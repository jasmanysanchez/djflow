


def crear_super_usuario_con_schema():
    from django.contrib.auth.models import User
    from tenant_schemas.utils import tenant_context
    from djflow.apps.tenant.models import Client
    from hmac import compare_digest
    from djflow.core.validaciones import email_es_valido
    schema_name=''
    existe = not Client.objects.filter(schema_name=schema_name).exists()
    while existe:
        schema_name = input('\033[0;34;50m Escriba el nombre de schema\033[0;30;50m\n')
        existe = not Client.objects.filter(schema_name=schema_name).exists()
        if existe:
            print("\033[0;31;50m No existe el schema '{}', intente nuevamente\033[0;30;50m".format(schema_name))
    tenant = Client.objects.get(schema_name=schema_name)
    username = ''
    username_existe = True
    while username_existe:
        username = input('\033[0;34;50m Escriba el nombre de usuario (username)\033[0;30;50m\n')
        with tenant_context(tenant):
            username_existe = User.objects.filter(username=username).exists()
        if username_existe:
            print("\033[0;31;50m El usuario '{}' ya existe, intente nuevamente\033[0;30;50m".format(username))
    email=''
    email_no_es_correcto = not email_es_valido(email)
    while email_no_es_correcto:
        email = input('\033[0;34;50m Escriba un correo electrónico para el usuario "{}"\033[0;30;50m\n'.format(username))
        email_no_es_correcto = not email_es_valido(email)
        if email_no_es_correcto:
            print("\033[0;31;50m EL correo electrónico no tiene un formato correcto\033[0;30;50m")
    contrasena_no_coincide = True
    password2=''
    while contrasena_no_coincide:
        password = input('\033[0;34;50m Escriba la contraseña para el usuario "{}"\033[0;30;50m\n'.format(username))
        password2 = input('\033[0;34;50m Escriba de nuevo la contraseña para el usuario "{}"\033[0;30;50m\n'.format(username))
        contrasena_no_coincide = not compare_digest(password, password2)
        if contrasena_no_coincide:
            print("\033[0;31;50m Las contraseñas no coinciden, intente nuevamente\033[0;30;50m")
    with tenant_context(tenant):
        user = User.objects.create_superuser(username=username, email=email, password=password2)
        if user:
            print("\033[0;32;50m El superusuario '{}' fue creado exitosamente\033[0;30;50m".format(username))