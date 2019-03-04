from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "INSERT INTO `petdb`.`pets` (`name`, `species`, `gender`, `birthday`) "
            "VALUES ('Fritz', 'dog', 'm', '2016-12-03');"
            "INSERT INTO `petdb`.`pets` (`name`, `species`, `gender`, `birthday`) "
            "VALUES ('Sweety', 'cat', 'w', '2015-06-23');"
            "INSERT INTO `petdb`.`pets` (`name`, `species`, `gender`, `birthday`) "
            "VALUES ('Tequila', 'parakeet', 'w', '2017-01-05');"
            "INSERT INTO `petdb`.`pets` (`name`, `species`, `gender`, `birthday`) "
            "VALUES ('Rambo', 'parakeet', 'm', NULL);"
            "INSERT INTO `petdb`.`pets` (`name`, `species`, `gender`, `birthday`) "
            "VALUES ('Smokey', 'cat', 'm', '2016-01-17');"
            "INSERT INTO `petdb`.`pets` (`name`, `species`, `gender`, `birthday`) "
            "VALUES ('Missy', 'dog', 'w', '2013-03-09');"
            # "INSERT INTO `petdb`.`pets` (`name`, `species`, `gender`, `birthday`) "
            # "VALUES ('Uni-🙈', 'monkey', 'm', '2014-04-01');"  # todo fix
        )
    ]
