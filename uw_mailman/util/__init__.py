from commonconf import override_settings

FMAILMAN = 'restclients.dao_implementation.mailman.File'
fdao_mailman_override = override_settings(
    RESTCLIENTS_MAILMAN_DAO_CLASS=FMAILMAN)
