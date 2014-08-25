# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(error_messages={b'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', b'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('time_zone', models.CharField(default=b'America/Chicago', max_length=30, choices=[(b'Africa', [(b'Africa/Abidjan', b'Abidjan'), (b'Africa/Accra', b'Accra'), (b'Africa/Addis_Ababa', b'Addis_Ababa'), (b'Africa/Algiers', b'Algiers'), (b'Africa/Asmara', b'Asmara'), (b'Africa/Bamako', b'Bamako'), (b'Africa/Bangui', b'Bangui'), (b'Africa/Banjul', b'Banjul'), (b'Africa/Bissau', b'Bissau'), (b'Africa/Blantyre', b'Blantyre'), (b'Africa/Brazzaville', b'Brazzaville'), (b'Africa/Bujumbura', b'Bujumbura'), (b'Africa/Cairo', b'Cairo'), (b'Africa/Casablanca', b'Casablanca'), (b'Africa/Ceuta', b'Ceuta'), (b'Africa/Conakry', b'Conakry'), (b'Africa/Dakar', b'Dakar'), (b'Africa/Dar_es_Salaam', b'Dar_es_Salaam'), (b'Africa/Djibouti', b'Djibouti'), (b'Africa/Douala', b'Douala'), (b'Africa/El_Aaiun', b'El_Aaiun'), (b'Africa/Freetown', b'Freetown'), (b'Africa/Gaborone', b'Gaborone'), (b'Africa/Harare', b'Harare'), (b'Africa/Johannesburg', b'Johannesburg'), (b'Africa/Juba', b'Juba'), (b'Africa/Kampala', b'Kampala'), (b'Africa/Khartoum', b'Khartoum'), (b'Africa/Kigali', b'Kigali'), (b'Africa/Kinshasa', b'Kinshasa'), (b'Africa/Lagos', b'Lagos'), (b'Africa/Libreville', b'Libreville'), (b'Africa/Lome', b'Lome'), (b'Africa/Luanda', b'Luanda'), (b'Africa/Lubumbashi', b'Lubumbashi'), (b'Africa/Lusaka', b'Lusaka'), (b'Africa/Malabo', b'Malabo'), (b'Africa/Maputo', b'Maputo'), (b'Africa/Maseru', b'Maseru'), (b'Africa/Mbabane', b'Mbabane'), (b'Africa/Mogadishu', b'Mogadishu'), (b'Africa/Monrovia', b'Monrovia'), (b'Africa/Nairobi', b'Nairobi'), (b'Africa/Ndjamena', b'Ndjamena'), (b'Africa/Niamey', b'Niamey'), (b'Africa/Nouakchott', b'Nouakchott'), (b'Africa/Ouagadougou', b'Ouagadougou'), (b'Africa/Porto-Novo', b'Porto-Novo'), (b'Africa/Sao_Tome', b'Sao_Tome'), (b'Africa/Tripoli', b'Tripoli'), (b'Africa/Tunis', b'Tunis'), (b'Africa/Windhoek', b'Windhoek')]), (b'America', [(b'America/Adak', b'Adak'), (b'America/Anchorage', b'Anchorage'), (b'America/Anguilla', b'Anguilla'), (b'America/Antigua', b'Antigua'), (b'America/Araguaina', b'Araguaina'), (b'America/Argentina/Buenos_Aires', b'Argentina - Buenos_Aires'), (b'America/Argentina/Catamarca', b'Argentina - Catamarca'), (b'America/Argentina/Cordoba', b'Argentina - Cordoba'), (b'America/Argentina/Jujuy', b'Argentina - Jujuy'), (b'America/Argentina/La_Rioja', b'Argentina - La_Rioja'), (b'America/Argentina/Mendoza', b'Argentina - Mendoza'), (b'America/Argentina/Rio_Gallegos', b'Argentina - Rio_Gallegos'), (b'America/Argentina/Salta', b'Argentina - Salta'), (b'America/Argentina/San_Juan', b'Argentina - San_Juan'), (b'America/Argentina/San_Luis', b'Argentina - San_Luis'), (b'America/Argentina/Tucuman', b'Argentina - Tucuman'), (b'America/Argentina/Ushuaia', b'Argentina - Ushuaia'), (b'America/Aruba', b'Aruba'), (b'America/Asuncion', b'Asuncion'), (b'America/Atikokan', b'Atikokan'), (b'America/Bahia', b'Bahia'), (b'America/Bahia_Banderas', b'Bahia_Banderas'), (b'America/Barbados', b'Barbados'), (b'America/Belem', b'Belem'), (b'America/Belize', b'Belize'), (b'America/Blanc-Sablon', b'Blanc-Sablon'), (b'America/Boa_Vista', b'Boa_Vista'), (b'America/Bogota', b'Bogota'), (b'America/Boise', b'Boise'), (b'America/Cambridge_Bay', b'Cambridge_Bay'), (b'America/Campo_Grande', b'Campo_Grande'), (b'America/Cancun', b'Cancun'), (b'America/Caracas', b'Caracas'), (b'America/Cayenne', b'Cayenne'), (b'America/Cayman', b'Cayman'), (b'America/Chicago', b'Chicago'), (b'America/Chihuahua', b'Chihuahua'), (b'America/Costa_Rica', b'Costa_Rica'), (b'America/Creston', b'Creston'), (b'America/Cuiaba', b'Cuiaba'), (b'America/Curacao', b'Curacao'), (b'America/Danmarkshavn', b'Danmarkshavn'), (b'America/Dawson', b'Dawson'), (b'America/Dawson_Creek', b'Dawson_Creek'), (b'America/Denver', b'Denver'), (b'America/Detroit', b'Detroit'), (b'America/Dominica', b'Dominica'), (b'America/Edmonton', b'Edmonton'), (b'America/Eirunepe', b'Eirunepe'), (b'America/El_Salvador', b'El_Salvador'), (b'America/Fortaleza', b'Fortaleza'), (b'America/Glace_Bay', b'Glace_Bay'), (b'America/Godthab', b'Godthab'), (b'America/Goose_Bay', b'Goose_Bay'), (b'America/Grand_Turk', b'Grand_Turk'), (b'America/Grenada', b'Grenada'), (b'America/Guadeloupe', b'Guadeloupe'), (b'America/Guatemala', b'Guatemala'), (b'America/Guayaquil', b'Guayaquil'), (b'America/Guyana', b'Guyana'), (b'America/Halifax', b'Halifax'), (b'America/Havana', b'Havana'), (b'America/Hermosillo', b'Hermosillo'), (b'America/Indiana/Indianapolis', b'Indiana - Indianapolis'), (b'America/Indiana/Knox', b'Indiana - Knox'), (b'America/Indiana/Marengo', b'Indiana - Marengo'), (b'America/Indiana/Petersburg', b'Indiana - Petersburg'), (b'America/Indiana/Tell_City', b'Indiana - Tell_City'), (b'America/Indiana/Vevay', b'Indiana - Vevay'), (b'America/Indiana/Vincennes', b'Indiana - Vincennes'), (b'America/Indiana/Winamac', b'Indiana - Winamac'), (b'America/Inuvik', b'Inuvik'), (b'America/Iqaluit', b'Iqaluit'), (b'America/Jamaica', b'Jamaica'), (b'America/Juneau', b'Juneau'), (b'America/Kentucky/Louisville', b'Kentucky - Louisville'), (b'America/Kentucky/Monticello', b'Kentucky - Monticello'), (b'America/Kralendijk', b'Kralendijk'), (b'America/La_Paz', b'La_Paz'), (b'America/Lima', b'Lima'), (b'America/Los_Angeles', b'Los_Angeles'), (b'America/Lower_Princes', b'Lower_Princes'), (b'America/Maceio', b'Maceio'), (b'America/Managua', b'Managua'), (b'America/Manaus', b'Manaus'), (b'America/Marigot', b'Marigot'), (b'America/Martinique', b'Martinique'), (b'America/Matamoros', b'Matamoros'), (b'America/Mazatlan', b'Mazatlan'), (b'America/Menominee', b'Menominee'), (b'America/Merida', b'Merida'), (b'America/Metlakatla', b'Metlakatla'), (b'America/Mexico_City', b'Mexico_City'), (b'America/Miquelon', b'Miquelon'), (b'America/Moncton', b'Moncton'), (b'America/Monterrey', b'Monterrey'), (b'America/Montevideo', b'Montevideo'), (b'America/Montreal', b'Montreal'), (b'America/Montserrat', b'Montserrat'), (b'America/Nassau', b'Nassau'), (b'America/New_York', b'New_York'), (b'America/Nipigon', b'Nipigon'), (b'America/Nome', b'Nome'), (b'America/Noronha', b'Noronha'), (b'America/North_Dakota/Beulah', b'North_Dakota - Beulah'), (b'America/North_Dakota/Center', b'North_Dakota - Center'), (b'America/North_Dakota/New_Salem', b'North_Dakota - New_Salem'), (b'America/Ojinaga', b'Ojinaga'), (b'America/Panama', b'Panama'), (b'America/Pangnirtung', b'Pangnirtung'), (b'America/Paramaribo', b'Paramaribo'), (b'America/Phoenix', b'Phoenix'), (b'America/Port-au-Prince', b'Port-au-Prince'), (b'America/Port_of_Spain', b'Port_of_Spain'), (b'America/Porto_Velho', b'Porto_Velho'), (b'America/Puerto_Rico', b'Puerto_Rico'), (b'America/Rainy_River', b'Rainy_River'), (b'America/Rankin_Inlet', b'Rankin_Inlet'), (b'America/Recife', b'Recife'), (b'America/Regina', b'Regina'), (b'America/Resolute', b'Resolute'), (b'America/Rio_Branco', b'Rio_Branco'), (b'America/Santa_Isabel', b'Santa_Isabel'), (b'America/Santarem', b'Santarem'), (b'America/Santiago', b'Santiago'), (b'America/Santo_Domingo', b'Santo_Domingo'), (b'America/Sao_Paulo', b'Sao_Paulo'), (b'America/Scoresbysund', b'Scoresbysund'), (b'America/Sitka', b'Sitka'), (b'America/St_Barthelemy', b'St_Barthelemy'), (b'America/St_Johns', b'St_Johns'), (b'America/St_Kitts', b'St_Kitts'), (b'America/St_Lucia', b'St_Lucia'), (b'America/St_Thomas', b'St_Thomas'), (b'America/St_Vincent', b'St_Vincent'), (b'America/Swift_Current', b'Swift_Current'), (b'America/Tegucigalpa', b'Tegucigalpa'), (b'America/Thule', b'Thule'), (b'America/Thunder_Bay', b'Thunder_Bay'), (b'America/Tijuana', b'Tijuana'), (b'America/Toronto', b'Toronto'), (b'America/Tortola', b'Tortola'), (b'America/Vancouver', b'Vancouver'), (b'America/Whitehorse', b'Whitehorse'), (b'America/Winnipeg', b'Winnipeg'), (b'America/Yakutat', b'Yakutat'), (b'America/Yellowknife', b'Yellowknife')]), (b'Antarctica', [(b'Antarctica/Casey', b'Casey'), (b'Antarctica/Davis', b'Davis'), (b'Antarctica/DumontDUrville', b'DumontDUrville'), (b'Antarctica/Macquarie', b'Macquarie'), (b'Antarctica/Mawson', b'Mawson'), (b'Antarctica/McMurdo', b'McMurdo'), (b'Antarctica/Palmer', b'Palmer'), (b'Antarctica/Rothera', b'Rothera'), (b'Antarctica/Syowa', b'Syowa'), (b'Antarctica/Vostok', b'Vostok')]), (b'Arctic', [(b'Arctic/Longyearbyen', b'Longyearbyen')]), (b'Asia', [(b'Asia/Aden', b'Aden'), (b'Asia/Almaty', b'Almaty'), (b'Asia/Amman', b'Amman'), (b'Asia/Anadyr', b'Anadyr'), (b'Asia/Aqtau', b'Aqtau'), (b'Asia/Aqtobe', b'Aqtobe'), (b'Asia/Ashgabat', b'Ashgabat'), (b'Asia/Baghdad', b'Baghdad'), (b'Asia/Bahrain', b'Bahrain'), (b'Asia/Baku', b'Baku'), (b'Asia/Bangkok', b'Bangkok'), (b'Asia/Beirut', b'Beirut'), (b'Asia/Bishkek', b'Bishkek'), (b'Asia/Brunei', b'Brunei'), (b'Asia/Choibalsan', b'Choibalsan'), (b'Asia/Chongqing', b'Chongqing'), (b'Asia/Colombo', b'Colombo'), (b'Asia/Damascus', b'Damascus'), (b'Asia/Dhaka', b'Dhaka'), (b'Asia/Dili', b'Dili'), (b'Asia/Dubai', b'Dubai'), (b'Asia/Dushanbe', b'Dushanbe'), (b'Asia/Gaza', b'Gaza'), (b'Asia/Harbin', b'Harbin'), (b'Asia/Hebron', b'Hebron'), (b'Asia/Ho_Chi_Minh', b'Ho_Chi_Minh'), (b'Asia/Hong_Kong', b'Hong_Kong'), (b'Asia/Hovd', b'Hovd'), (b'Asia/Irkutsk', b'Irkutsk'), (b'Asia/Jakarta', b'Jakarta'), (b'Asia/Jayapura', b'Jayapura'), (b'Asia/Jerusalem', b'Jerusalem'), (b'Asia/Kabul', b'Kabul'), (b'Asia/Kamchatka', b'Kamchatka'), (b'Asia/Karachi', b'Karachi'), (b'Asia/Kashgar', b'Kashgar'), (b'Asia/Kathmandu', b'Kathmandu'), (b'Asia/Khandyga', b'Khandyga'), (b'Asia/Kolkata', b'Kolkata'), (b'Asia/Krasnoyarsk', b'Krasnoyarsk'), (b'Asia/Kuala_Lumpur', b'Kuala_Lumpur'), (b'Asia/Kuching', b'Kuching'), (b'Asia/Kuwait', b'Kuwait'), (b'Asia/Macau', b'Macau'), (b'Asia/Magadan', b'Magadan'), (b'Asia/Makassar', b'Makassar'), (b'Asia/Manila', b'Manila'), (b'Asia/Muscat', b'Muscat'), (b'Asia/Nicosia', b'Nicosia'), (b'Asia/Novokuznetsk', b'Novokuznetsk'), (b'Asia/Novosibirsk', b'Novosibirsk'), (b'Asia/Omsk', b'Omsk'), (b'Asia/Oral', b'Oral'), (b'Asia/Phnom_Penh', b'Phnom_Penh'), (b'Asia/Pontianak', b'Pontianak'), (b'Asia/Pyongyang', b'Pyongyang'), (b'Asia/Qatar', b'Qatar'), (b'Asia/Qyzylorda', b'Qyzylorda'), (b'Asia/Rangoon', b'Rangoon'), (b'Asia/Riyadh', b'Riyadh'), (b'Asia/Sakhalin', b'Sakhalin'), (b'Asia/Samarkand', b'Samarkand'), (b'Asia/Seoul', b'Seoul'), (b'Asia/Shanghai', b'Shanghai'), (b'Asia/Singapore', b'Singapore'), (b'Asia/Taipei', b'Taipei'), (b'Asia/Tashkent', b'Tashkent'), (b'Asia/Tbilisi', b'Tbilisi'), (b'Asia/Tehran', b'Tehran'), (b'Asia/Thimphu', b'Thimphu'), (b'Asia/Tokyo', b'Tokyo'), (b'Asia/Ulaanbaatar', b'Ulaanbaatar'), (b'Asia/Urumqi', b'Urumqi'), (b'Asia/Ust-Nera', b'Ust-Nera'), (b'Asia/Vientiane', b'Vientiane'), (b'Asia/Vladivostok', b'Vladivostok'), (b'Asia/Yakutsk', b'Yakutsk'), (b'Asia/Yekaterinburg', b'Yekaterinburg'), (b'Asia/Yerevan', b'Yerevan')]), (b'Atlantic', [(b'Atlantic/Azores', b'Azores'), (b'Atlantic/Bermuda', b'Bermuda'), (b'Atlantic/Canary', b'Canary'), (b'Atlantic/Cape_Verde', b'Cape_Verde'), (b'Atlantic/Faroe', b'Faroe'), (b'Atlantic/Madeira', b'Madeira'), (b'Atlantic/Reykjavik', b'Reykjavik'), (b'Atlantic/South_Georgia', b'South_Georgia'), (b'Atlantic/St_Helena', b'St_Helena'), (b'Atlantic/Stanley', b'Stanley')]), (b'Australia', [(b'Australia/Adelaide', b'Adelaide'), (b'Australia/Brisbane', b'Brisbane'), (b'Australia/Broken_Hill', b'Broken_Hill'), (b'Australia/Currie', b'Currie'), (b'Australia/Darwin', b'Darwin'), (b'Australia/Eucla', b'Eucla'), (b'Australia/Hobart', b'Hobart'), (b'Australia/Lindeman', b'Lindeman'), (b'Australia/Lord_Howe', b'Lord_Howe'), (b'Australia/Melbourne', b'Melbourne'), (b'Australia/Perth', b'Perth'), (b'Australia/Sydney', b'Sydney')]), (b'Canada', [(b'Canada/Atlantic', b'Atlantic'), (b'Canada/Central', b'Central'), (b'Canada/Eastern', b'Eastern'), (b'Canada/Mountain', b'Mountain'), (b'Canada/Newfoundland', b'Newfoundland'), (b'Canada/Pacific', b'Pacific')]), (b'Europe', [(b'Europe/Amsterdam', b'Amsterdam'), (b'Europe/Andorra', b'Andorra'), (b'Europe/Athens', b'Athens'), (b'Europe/Belgrade', b'Belgrade'), (b'Europe/Berlin', b'Berlin'), (b'Europe/Bratislava', b'Bratislava'), (b'Europe/Brussels', b'Brussels'), (b'Europe/Bucharest', b'Bucharest'), (b'Europe/Budapest', b'Budapest'), (b'Europe/Busingen', b'Busingen'), (b'Europe/Chisinau', b'Chisinau'), (b'Europe/Copenhagen', b'Copenhagen'), (b'Europe/Dublin', b'Dublin'), (b'Europe/Gibraltar', b'Gibraltar'), (b'Europe/Guernsey', b'Guernsey'), (b'Europe/Helsinki', b'Helsinki'), (b'Europe/Isle_of_Man', b'Isle_of_Man'), (b'Europe/Istanbul', b'Istanbul'), (b'Europe/Jersey', b'Jersey'), (b'Europe/Kaliningrad', b'Kaliningrad'), (b'Europe/Kiev', b'Kiev'), (b'Europe/Lisbon', b'Lisbon'), (b'Europe/Ljubljana', b'Ljubljana'), (b'Europe/London', b'London'), (b'Europe/Luxembourg', b'Luxembourg'), (b'Europe/Madrid', b'Madrid'), (b'Europe/Malta', b'Malta'), (b'Europe/Mariehamn', b'Mariehamn'), (b'Europe/Minsk', b'Minsk'), (b'Europe/Monaco', b'Monaco'), (b'Europe/Moscow', b'Moscow'), (b'Europe/Oslo', b'Oslo'), (b'Europe/Paris', b'Paris'), (b'Europe/Podgorica', b'Podgorica'), (b'Europe/Prague', b'Prague'), (b'Europe/Riga', b'Riga'), (b'Europe/Rome', b'Rome'), (b'Europe/Samara', b'Samara'), (b'Europe/San_Marino', b'San_Marino'), (b'Europe/Sarajevo', b'Sarajevo'), (b'Europe/Simferopol', b'Simferopol'), (b'Europe/Skopje', b'Skopje'), (b'Europe/Sofia', b'Sofia'), (b'Europe/Stockholm', b'Stockholm'), (b'Europe/Tallinn', b'Tallinn'), (b'Europe/Tirane', b'Tirane'), (b'Europe/Uzhgorod', b'Uzhgorod'), (b'Europe/Vaduz', b'Vaduz'), (b'Europe/Vatican', b'Vatican'), (b'Europe/Vienna', b'Vienna'), (b'Europe/Vilnius', b'Vilnius'), (b'Europe/Volgograd', b'Volgograd'), (b'Europe/Warsaw', b'Warsaw'), (b'Europe/Zagreb', b'Zagreb'), (b'Europe/Zaporozhye', b'Zaporozhye'), (b'Europe/Zurich', b'Zurich')]), (b'Indian', [(b'Indian/Antananarivo', b'Antananarivo'), (b'Indian/Chagos', b'Chagos'), (b'Indian/Christmas', b'Christmas'), (b'Indian/Cocos', b'Cocos'), (b'Indian/Comoro', b'Comoro'), (b'Indian/Kerguelen', b'Kerguelen'), (b'Indian/Mahe', b'Mahe'), (b'Indian/Maldives', b'Maldives'), (b'Indian/Mauritius', b'Mauritius'), (b'Indian/Mayotte', b'Mayotte'), (b'Indian/Reunion', b'Reunion')]), (b'Pacific', [(b'Pacific/Apia', b'Apia'), (b'Pacific/Auckland', b'Auckland'), (b'Pacific/Chatham', b'Chatham'), (b'Pacific/Chuuk', b'Chuuk'), (b'Pacific/Easter', b'Easter'), (b'Pacific/Efate', b'Efate'), (b'Pacific/Enderbury', b'Enderbury'), (b'Pacific/Fakaofo', b'Fakaofo'), (b'Pacific/Fiji', b'Fiji'), (b'Pacific/Funafuti', b'Funafuti'), (b'Pacific/Galapagos', b'Galapagos'), (b'Pacific/Gambier', b'Gambier'), (b'Pacific/Guadalcanal', b'Guadalcanal'), (b'Pacific/Guam', b'Guam'), (b'Pacific/Honolulu', b'Honolulu'), (b'Pacific/Johnston', b'Johnston'), (b'Pacific/Kiritimati', b'Kiritimati'), (b'Pacific/Kosrae', b'Kosrae'), (b'Pacific/Kwajalein', b'Kwajalein'), (b'Pacific/Majuro', b'Majuro'), (b'Pacific/Marquesas', b'Marquesas'), (b'Pacific/Midway', b'Midway'), (b'Pacific/Nauru', b'Nauru'), (b'Pacific/Niue', b'Niue'), (b'Pacific/Norfolk', b'Norfolk'), (b'Pacific/Noumea', b'Noumea'), (b'Pacific/Pago_Pago', b'Pago_Pago'), (b'Pacific/Palau', b'Palau'), (b'Pacific/Pitcairn', b'Pitcairn'), (b'Pacific/Pohnpei', b'Pohnpei'), (b'Pacific/Port_Moresby', b'Port_Moresby'), (b'Pacific/Rarotonga', b'Rarotonga'), (b'Pacific/Saipan', b'Saipan'), (b'Pacific/Tahiti', b'Tahiti'), (b'Pacific/Tarawa', b'Tarawa'), (b'Pacific/Tongatapu', b'Tongatapu'), (b'Pacific/Wake', b'Wake'), (b'Pacific/Wallis', b'Wallis')])])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
