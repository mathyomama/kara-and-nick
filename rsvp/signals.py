from django.db.models import signals
from django.contrib.auth.models import Group, Permission

# This is a dictionary for which holds the groups and the permissions for each group
wedding_group_permissions = {
        "Guest": [
            "add_guestbookentry",
            ],
        }

# This is the function that will create the groups after the migration is done
def create_user_groups(sender, created_models, verbosity, **kwargs):
    if verbosity > 0:
        print "Initializing data post_migrate"
    for group in wedding_group_permissions:
        selected_group, created = Group.objects.get_or_create(name=group)
        if verbosity > 1 and created:
            print "Creating group '%s'." % group
        for perm in wedding_group_permissions[group]:
            p = Permission.objects.get(codename=perm)
            selected_group.permissions.add(p)
            if verbosity > 1:
                print "Permitting '%s' to '%s'." % (group, p.name)
        selected_group.save()

def test_function(sender, **kwargs):
    print "This is a test after the migration"

# For Accounts
def put_account_into_guest(sender, instance, **kwargs):
    instance.user.groups.add(Group.objects.get(name='Guest'))
    instance.user.save()
    print "Added %s to 'Guest'." % instance.user
