# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 03:08
from __future__ import unicode_literals

import apps.users.models.user
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=20, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('nickname', models.CharField(blank=True, help_text='Azar 내에서 다른 사용자들을 검색하는데 필요한 고유 Azar ID', max_length=20, null=True, unique=True)),
                ('birth_year', models.PositiveSmallIntegerField(blank=True, choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unspecified')], max_length=1)),
                ('country', models.CharField(choices=[('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AG', 'Antigua and Barbuda'), ('AI', 'Anguilla'), ('AL', 'Albania'), ('AM', 'Armenia'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AR', 'Argentina'), ('AS', 'American Samoa'), ('AT', 'Austria'), ('AU', 'Australia'), ('AW', 'Aruba'), ('AX', 'Åland Islands'), ('AZ', 'Azerbaijan'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BL', 'Saint Barthélemy'), ('BM', 'Bermuda'), ('BN', 'Brunei Darussalam'), ('BO', 'Bolivia, Plurinational State of'), ('BQ', 'Caribbean Netherlands'), ('BR', 'Brazil'), ('BS', 'Bahamas'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CD', 'Congo, the Democratic Republic of the'), ('CF', 'Central African Republic'), ('CG', 'Congo'), ('CH', 'Switzerland'), ('CI', "Côte d'Ivoire"), ('CK', 'Cook Islands'), ('CL', 'Chile'), ('CM', 'Cameroon'), ('CN', 'China'), ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CV', 'Cape Verde'), ('CW', 'Curaçao'), ('CX', 'Christmas Island'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ES', 'Spain'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FM', 'Micronesia, Federated States of'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('GA', 'Gabon'), ('GB-ENG', 'England'), ('GB-NIR', 'Northern Ireland'), ('GB-SCT', 'Scotland'), ('GB-WLS', 'Wales'), ('GB', 'United Kingdom'), ('GD', 'Grenada'), ('GE', 'Georgia'), ('GF', 'French Guiana'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GL', 'Greenland'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GT', 'Guatemala'), ('GU', 'Guam'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard Island and McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IM', 'Isle of Man'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Iran, Islamic Republic of'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JE', 'Jersey'), ('JM', 'Jamaica'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KM', 'Comoros'), ('KN', 'Saint Kitts and Nevis'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KY', 'Cayman Islands'), ('KZ', 'Kazakhstan'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('LY', 'Libya'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('ME', 'Montenegro'), ('MF', 'Saint Martin'), ('MG', 'Madagascar'), ('MH', 'Marshall Islands'), ('MK', 'Macedonia, the former Yugoslav Republic of'), ('ML', 'Mali'), ('MM', 'Myanmar'), ('MN', 'Mongolia'), ('MO', 'Macao'), ('MP', 'Northern Mariana Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MS', 'Montserrat'), ('MT', 'Malta'), ('MU', 'Mauritius'), ('MV', 'Maldives'), ('MW', 'Malawi'), ('MX', 'Mexico'), ('MY', 'Malaysia'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PA', 'Panama'), ('PE', 'Peru'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PL', 'Poland'), ('PM', 'Saint Pierre and Miquelon'), ('PN', 'Pitcairn'), ('PR', 'Puerto Rico'), ('PS', 'Palestine'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PY', 'Paraguay'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RS', 'Serbia'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SB', 'Solomon Islands'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SE', 'Sweden'), ('SG', 'Singapore'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SI', 'Slovenia'), ('SJ', 'Svalbard and Jan Mayen Islands'), ('SK', 'Slovakia'), ('SL', 'Sierra Leone'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SR', 'Suriname'), ('SS', 'South Sudan'), ('ST', 'Sao Tome and Principe'), ('SV', 'El Salvador'), ('SX', 'Sint Maarten (Dutch part)'), ('SY', 'Syrian Arab Republic'), ('SZ', 'Swaziland'), ('TC', 'Turks and Caicos Islands'), ('TD', 'Chad'), ('TF', 'French Southern Territories'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TL', 'Timor-Leste'), ('TM', 'Turkmenistan'), ('TN', 'Tunisia'), ('TO', 'Tonga'), ('TR', 'Turkey'), ('TT', 'Trinidad and Tobago'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UA', 'Ukraine'), ('UG', 'Uganda'), ('UM', 'US Minor Outlying Islands'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VA', 'Holy See (Vatican City State)'), ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna Islands'), ('XK', 'Kosovo'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('YT', 'Mayotte'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('time_zone', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=10)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile/')),
                ('gem_total_count', models.IntegerField(default=0)),
                ('is_facebook_user', models.BooleanField(default=False)),
                ('is_vip', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', apps.users.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FacebookUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_user_id', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FriendInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ManagedFriendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('BM', 'Bookmarked'), ('HD', 'Hidden'), ('BL', 'Blocked')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('VA', 'Verbal Abuse'), ('SA', 'Sexual Abuse')], max_length=2)),
                ('screenshot', models.ImageField(blank=True, upload_to='report-screenshot/')),
            ],
        ),
        migrations.CreateModel(
            name='ThumbsUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VipUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.AddField(
            model_name='thumbsup',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbsup_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='thumbsup',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbsup_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='managedfriendship',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_friendship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='managedfriendship',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendinvitation',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_invitation_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendinvitation',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_invitation_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facebookuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='facebook_user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_user_friends_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='who_friend_request_to',
            field=models.ManyToManyField(blank=True, related_name='who_friend_request_from', through='users.FriendInvitation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='who_report_to',
            field=models.ManyToManyField(blank=True, related_name='who_report_from', through='users.Report', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='who_thumbsup_to',
            field=models.ManyToManyField(blank=True, related_name='who_thumbsup_from', through='users.ThumbsUp', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='thumbsup',
            unique_together=set([('source', 'target')]),
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=set([('source', 'target')]),
        ),
        migrations.AlterUniqueTogether(
            name='managedfriendship',
            unique_together=set([('source', 'target')]),
        ),
        migrations.AlterUniqueTogether(
            name='friendinvitation',
            unique_together=set([('source', 'target')]),
        ),
    ]