# from .json_settings import get_settings
# import os
#
# __PATH_MEDIA = os.path.dirname(os.path.dirname(__file__))
# LOGGIN_ROOT = os.path.join(__PATH_MEDIA, '../log')
#
# settings = get_settings()
#
# settings["LOGGING"]["DEBUG_PATH"] = eval(settings["LOGGING"]["DEBUG_PATH"])
# settings["LOGGING"]["ERROR_PATH"] = eval(settings["LOGGING"]["ERROR_PATH"])
# settings["LOGGING"]["DJFLOW_PATH"] = eval(settings["LOGGING"]["DJFLOW_PATH"])
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'tenant_context': {
#             'format': '[%(schema_name)s:%(domain_url)s] '
#                       '%(levelname)-7s %(asctime)s %(message)s',
#         },
#     },
#     'filters': {
#         'tenant_context': {
#             '()': 'tenant_schemas.log.TenantContextFilter'
#         },
#     },
#     'handlers': {
#         'debug_file': {
#             'level': 'DEBUG',
#             'filters': ['tenant_context'],
#             'class': 'logging.FileHandler',
#             'filename': settings["LOGGING"]["DEBUG_PATH"],
#             'formatter': 'tenant_context'
#         },
#         'error_file': {
#             'level': 'ERROR',
#             'filters': ['tenant_context'],
#             'class': 'logging.FileHandler',
#             'filename': settings["LOGGING"]["ERROR_PATH"],
#             'formatter': 'tenant_context'
#         },
#         'djflow_file': {
#             'filters': ['tenant_context'],
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': settings["LOGGING"]["DJFLOW_PATH"],
#             'formatter': 'tenant_context'
#         },
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['tenant_context'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'tenant_context',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'error_file'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['debug_file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'djflow': {
#             'handlers': ['console', 'djflow_file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         }
#     },
# }
