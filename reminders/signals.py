from django.db.models import Q
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver, Signal

from events.models import Attendance, Event
from reminders.models import Prompt
from reminders import tasks

import logging
logger = logging.getLogger(__name__)

update_attendance = Signal()
update_event = Signal()

@receiver(update_attendance)
@receiver(post_save, sender=Attendance)
def attendance_prompts_schedule(sender, **kwargs):
    attendance = kwargs['instance']
    created = kwargs.get('created', False)
    update_fields = kwargs.get('update_fields', {})

    if created or (update_fields and 'event' in update_fields):
        logger.info('attendance_prompts_schedule: %s' % attendance.id)
        tasks.schedule_attendance_prompts(attendance)
    else:
        # updated with response data, don't schedule prompts
        pass

@receiver(post_delete, sender=Attendance)
def attendance_prompts_clear(sender, **kwargs):
    attendance = kwargs['instance']
    logger.info('attendance_prompts_clear: %s' % attendance.id)
    tasks.schedule_clear_prompts(attendance)

@receiver(update_event)
@receiver(post_save, sender=Event)
def event_prompts_reset(sender, **kwargs):
    event = kwargs['instance']
    logger.info('attendance_prompts_reset: %s' % event.id)
    for a in event.attendance_set.all():
        Signal.send(update_attendance, sender=Attendance, instance=a, update_fields=['event'])

@receiver(post_save, sender=Prompt)
def update_prompts(sender, **kwargs):
    prompt = kwargs['instance']
    logger.info('update_prompts: %s' % prompt.id)
    for e in Event.objects.filter(Q(prompt_before=prompt) | Q(prompt_after=prompt)):
        Signal.send(update_event, sender=Event, instance=e)
