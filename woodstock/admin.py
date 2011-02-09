from woodstock.models import Event, EventAdmin,\
    Participant, ParticipantAdmin, Invitee, InviteeAdmin, Group, GroupAdmin,\
    Salutation, SalutationAdmin
from woodstock import settings

from django.contrib import admin

if settings.ADMIN_HAS_EVENT:
    admin.site.register(Event, EventAdmin)
if settings.ADMIN_HAS_PARTICIPANT:
    admin.site.register(Participant, ParticipantAdmin)
if settings.ADMIN_HAS_GROUP:
    admin.site.register(Group,GroupAdmin)
if settings.ADMIN_HAS_INVITEE:
    admin.site.register(Invitee, InviteeAdmin)
if settings.ADMIN_HAS_SALUTATION:
    admin.site.register(Salutation, SalutationAdmin)
