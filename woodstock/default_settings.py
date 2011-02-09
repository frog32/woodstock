from django.conf import settings

LANGUAGES = getattr(settings, 'LANGUAGES')
LANGUAGE_CODE = getattr(settings, 'LANGUAGE_CODE')

INVITEE_GENERATES_PASSWORD = getattr(settings, 'WOODSTOCK_INVITEE_GENERATES_PASSWORD', False)

SUBSCRIPTION_NEEDS_INVITATION = getattr(settings, 'WOODSTOCK_SUBSCRIPTION_NEEDS_INVITATION', False)
SUBSCRIPTION_CONSUMES_INVITATION = getattr(settings, 'WOODSTOCK_SUBSCRIPTION_CONSUMES_INVITATION', False)
SUBSCRIPTION_ALLOW_MULTIPLE_EVENTS = getattr(settings, 'WOODSTOCK_SUBSCRIPTION_ALLOW_MULTIPLE_EVENTS', True)
SUBSCRIPTION_ALLOW_MULTIPLE_EVENTPARTS = getattr(settings, 'WOODSTOCK_SUBSCRIPTION_ALLOW_MULTIPLE_EVENTPARTS', True)
SUBSCRIPTION_NEEDS_ACTIVATION = getattr(settings, 'WOODSTOCK_SUBSCRIPTION_NEEDS_ACTIVATION', False)

OVERBOOKING_ALLOWED = getattr(settings, 'WOODSTOCK_OVERBOOKING_ALLOWED', False)

# if set to None only password will be used
USERNAME_FIELD = getattr(settings, 'WOODSTOCK_USERNAME_FIELD', 'email')

PERSON_EMAIL_UNIQUE = getattr(settings, 'WOODSTOCK_PARTICIPANT_EMAIL_UNIQUE', True)

LOST_PASSWORD_NEWSLETTER = getattr(settings, 'WOODSTOCK_LOST_PASSWORD_NEWSLETTER', 'LOST PASSWORD')
ACTIVATION_NEWSLETTER = getattr(settings, 'WOODSTOCK_ACTIVATION_NEWSLETTER', 'ACTIVATION')

# customize admin view
ADMIN_HAS_PARTICIPANT = getattr(settings, 'WOODSTOCK_ADMIN_HAS_PARTICIPANT', True)
ADMIN_HAS_EVENT = getattr(settings, 'WOODSTOCK_ADMIN_HAS_EVENT', True)
ADMIN_HAS_INVITEE = getattr(settings, 'WOODSTOCK_ADMIN_HAS_INVITEE', True)
ADMIN_HAS_GROUP = getattr(settings, 'WOODSTOCK_ADMIN_HAS_GROUP', True)
ADMIN_HAS_SALUTATION = getattr(settings, 'WOODSTOCK_ADMIN_HAS_SALUTATION', True)