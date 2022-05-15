a = []
b = []
c = []
d = []
e = []
f = []
name = []


#Приветствие
greeting = 'Привет✋👋\n' \
       '\n'\
'\tСегодня вы проходите День в музее. Вы находитесь в очень интересном месте. Наверное, все вы знаете хоть что-то про Великую Отечественную войну. Музей, что носит название Победа, скорее всего, связан с этой войной. Так давайте посмотрим на историю здания, в котором вы сейчас находитесь...\n' \
       '\n'\
'\tОфициальное открытие музея состоялось 9 мая 1995 года. На это торжество прибыло 55 делегаций из различных государств, руководители которых оставили записи в Книге почёта. Военный парад, посвященный 50-летию Победы, в тот год проводился не только, как обычно, на Красной площади, но и на Поклонной горе. Вечером на Поклонной горе был дан грандиозный салют, а фасадная часть музея стала экраном, на который проецировались лучшие фильмы о войне, фотографии Сражений и ветеранов.' \

#Начальные фразы
begin_phrases = ['Скоро будет готов!', 'В процессе разработки...', 'Усердно работаем!', 'Совсем скоро...']

#Залы
hal_1 = ' ℹ️ Би́тва за Днепр — ряд взаимосвязанных стратегических операций Великой Отечественной войны, проведённых СССР, во второй половине 1943 года на берегах Днепра.\n'\
'С обеих сторон в битве приняло участие до 4 млн человек, а её фронт растянулся на 750 километров. В результате четырехмесячной операции Левобережная Украина была почти полностью освобождена Красной армией от нацистских захватчиков. В ходе операции значительные силы Красной Армии форсировали реку, создали несколько стратегических плацдармов на правом берегу реки, а также освободили город Киев. Битва за Днепр стала одним из крупнейших сражений в мировой истории.\n'\

hall_6 = ' ℹ Штурм Берлина — завершающая часть Берлинской наступательной операции, в ходе которой Красная армия завладела столицей нацистской Германии. Операция по взятию Берлина продолжалась с 16 апреля по 2 мая. В 12 часов дня 25 апреля 6-й гвардейский мехкорпус 4-й гвардейской танковой армии 1-го Украинского фронта форсировал реку Хафель и соединился с частями 328-й дивизии 47-й армии 1-го Белорусского фронта, замкнув тем самым кольцо окружения вокруг Берлина.\n'\
'К исходу 25 апреля гарнизон Берлина оборонялся на площади около 327 км². Общая протяжённость фронта советских войск в Берлине составляла около 100 км.\n'\
'Берлинская группировка, по оценке советского командования, насчитывала около 200 тыс. солдат и офицеров, 3 тыс. орудий и 250 танков. Оборона города была тщательно продумана и отлично подготовлена. В основе лежала система сильного огня, опорных пунктов и узлов сопротивления. В Берлине было создано девять секторов обороны — восемь по окружности и один в центре. Особую прочность ей придавали массивные каменные постройки с большой толщиной стен. Улицы перекрывались мощными баррикадами толщиною до четырёх метров. Немаловажное значение в немецкой системе обороны имели подземные сооружения, в том числе и метро.\n'

hall_3 = ' ℹ Ку́рская битва — это сразу несколько оборонительных и наступательных операций советских войск против немецко-фашистских захватчиков. По своим масштабам, задействованным силам и средствам, напряжённости, результатам и военно-политическим последствиям является одним из ключевых сражений Второй мировой войны и Великой Отечественной войны. Битва продолжалась 50 дней. Немецкая сторона наступательную часть сражения называла операция «Цитадель».'

hall_4 = ' ℹ 18 декабря 1940 года Гитлер подписал директиву, известную как План «Барбаросса». Этот план предусматривал нападение на СССР по направлениям, одно из которых включало Ленинград. Город был вторым по значению объектом в СССР с населением около 3,2 млн человек. С захватом Ленинграда немецкое командование могло бы разрешить ряд важных задач.'

hall_5 = ' ℹ Сталингра́дская би́тва — одно из важнейших и крупнейших генеральных сражений Второй мировой и Великой Отечественной войн.\n'\
'Наступление войск нацистской Германии и её союзников продолжалось с июля по ноябрь 1942 года. Осуществление этого плана блокировало бы транспортное сообщение между центральными районами СССР и Кавказом.\n'\
'За июль-ноябрь 1942 года Красной армии удалось заставить противника увязнуть в оборонительных боях, а до февраля 1943 года — окружить группировку немецко-фашистских войск, отбить деблокирующий немецкий удар и сжать кольцо окружения к развалинам Сталинграда.\n'

hall_2 = ' ℹ Битва за Москву включала в себя Московскую стратегическую оборонительную операцию.\n'\
'5 декабря 1941 года Красная армия перешла в контрнаступление по всему фронту под Москвой, проведя при этом ряд успешных фронтовых наступательных операций и отбросила немцев на 150-300 километров от столицы.\n'\
'5 декабря — день начала советского контрнаступления под Москвой — является одним из дней воинской славы России.\n'

room_1 = ''
room_2 = ''
room_3 = ''
room_4 = ''
room_5 = ''
room_6 = ''

#Вопросы зала (форсирование днепра)
qw_1 = '➖ Напишите, что указано на табличке-указателе:\n'\
       '\n'\
       '❓ 1. “Даешь Киев”\n' \
       '❓ 2. Смерть оккупантам \n' \
       '❓ 3. Слава Сталину\n' \
       '❓ 4. За Татарстан \n'

qw_2 = '➖ Найдите на стене летящий самолет и укажите его номер:\n' \
       '\n'\
       'Введите ответ:'

qw_3 = '➖ На интерактивном дисплее прочитайте историю Зины Портновой. Расставьте события жизни Зины в хронологическом порядке.\n' \
       '\n'\
       '❓ 1. (Рождение(дата)- 20 февраля 1926\n' \
       'Рождение(город)- Ленинград\n' \
       'Год вступления в  Обольскую подпольную организацию «Юные мстители» - 1942\n' \
       'Дата смерти - 10 января 1944)\n' \
       '\n'\
       '❓ 2. (Рождение(дата)- 20 января 1926\n' \
       'Рождение(город)- Ленинград\n' \
       'Год вступления в  Обольскую подпольную организацию «Юные мстители» - 1942\n' \
       'Дата смерти - 10 января 1944)\n' \
       '\n'\
       '❓ 3. (Рождение(дата)- 20 января 1928\n' \
       'Рождение(город)- Ленинград\n' \
       'Год вступления в  Обольскую подпольную организацию «Юные мстители» - 1940\n' \
       'Дата смерти - 10 января 1944)\n' \
       '\n'\
       '❓ 4. (Рождение(дата)- 20 января 1920\n' \
       'Рождение(город) - Ленинград\n' \
       'Год вступления в  Обольскую подпольную организацию «Зрелые разведчики» - 1942\n' \
       'Дата смерти - 10 января 1944)\n' \

qw_4 = "➖ Какой период лежит в основе диорамы?\n" \
       '\n'\
       '❓ 1. Сентябрь-октябрь 1943 года\n' \
       '❓ 2. Ноябрь-декабрь 1943 года\n' \
       '❓ 3. Сентябрь-ноябрь 1945 года\n' \
       '❓ 4. Январь-март 1941 года\n'

qw_5 = '➖ Как вы думаете, почему художник изобразил солнце над нашими войсками?\n'\
       '\n'\
       '❓ 1. Символизм данного фрагмента должен показать зрителю, что обещание скорой победы за нами\n' \
       '❓ 2. В тот день у художника было хорошее настроение\n' \
       '❓ 3. Солнце - символ окончания войны\n' \
       '❓ 4. Солнце символизирует светлое будущее\n'

#Справки для вопросов (форсирование днепра)
reference_1 = ' ‼ Указатели во время ВОВ использовались советскими гражданами не только по назначению, но и для дезориентирования сил Вермахта на местности. Даже такая маленькая вещь как перевернутый указатель могла перевернуть ход сражения. '
reference_2 = ' ‼ В воздушных боях участвовали более 2800 самолетов, среди них — истребители «Як», «Ла-5», «Аэрокобра», штурмовики «Ил-2». Против них немцы выставили новейшие модели истребителей «Фокке-Вульф FW-190» и «Мессершмитт Bf 109», которыми управляли опытнейшие воздушные асы немецкой армии'
reference_3 = ' ‼ Зинаида Портнова пионер-герой, советская подпольщица, партизанка со интересной и захватывающей историей. Подробнее о ней и других героях ВОВ вы можете прочитать на интерактивном дисплее'
reference_4 = ' ‼ После завершения Курской битвы вермахт потерял всякую надежду на решительную победу над СССР. Потери были значительными, и, что хуже, армия в целом была гораздо менее опытна, чем раньше, так как лучшие бойцы пали в предыдущих сражениях.'
reference_5 = ' ‼ Во время войны, многие картины были трофеями, которые попали на стены наших музеев. Но на фронте были так же и художники, которые рисовали на обшивке танков и другой технике что то значимое для экипажа или отделения '

#Вопросы зала (Контрнаступление под Москвой)
qwe_1 = '➖ Как вы думаете, почему солдаты в левой части диорамы одеты в белое?\n'\
       '\n'\
       '❓ 1.Модный цвет\n' \
       '❓ 2.Дефицит ткани другого цвета\n' \
       '❓ 3.Личное пожелание состава\n' \
       '❓ 4.На улица зима, масхалаты должны быть в цвет окружающей обстановке\n'

qwe_2 = '➖ Кто автор данной диорамы?\n'\
       '\n'\
       '❓ 1.Александр Иванович Данилов\n' \
       '❓ 2.Евгений Иванович Петровский\n' \
       '❓ 3.Владимир Дмитриевич Бочкарев\n' \
       '❓ 4.Евгений Иванович Данилевский\n'

qwe_3 = '➖ В каком округе происходят события данной диорамы?\n'\
       '\n'\
       '❓ 1.Район Раменки Московской области\n' \
       '❓ 2.Котельники, район Москвы\n' \
       '❓ 3.Город Клин Московская области\n' \
       '❓ 4.Яхрома Дмитровского района Московской области\n'

qwe_4 = '➖ Какова протяженность Можайской линии обороны?\n'\
       '\n'\
       '❓ 1.220 км\n' \
       '❓ 2.250 км\n' \
       '❓ 3.100 км\n' \
       '❓ 4.220 м\n'

#Справки для вопросов (Контрнаступление под Москвой)
referen_1 = '‼ Маскировочный халат — один из вариантов камуфляжной специальной одежды. Как правило, ткань таких костюмов более тонкая, чем ткань уставной формы, но не всегда она менее прочная.\n'\
'Изначально это были маскхалаты и накидки пятнистой окраски четырех цветовых гамм: лето, весна-осень, пустыня и для горных районов. В отдельном ряду идут белые маскхалаты для зимнего камуфляжа'

referen_2 = ' ‼ Евгений Иванович Данилевский Окончил Харьковский художественный институт в 1952 году по мастерской батальной живописи.\n'\
'С 1952 года работал в Москве над монументальными произведениями для ВДНХ, в комбинате живописного искусства Художественного фонда РСФСР.\n'\
'Участник большинства республиканских и всесоюзных выставок 1960-80-х годов.\n'\
'Автор многочисленных живописных полотен на исторические темы — «Куликовская битва», «Дмитрий Донской» и др.'

referen_3 = ' ‼ Наши войска остановили вражеское полчища у стен советской столицы, а затем нанесли сокрушительное поражение немецко-фашистским армиям. Именно под Москвой был развеян миф о непобедимости гитлеровских войск и было положено начало коренному повороту в ходе всей Второй Мировой Войны.'

referen_4 = ' ‼ Можайская линия обороны - рубеж, создававшийся в 1941 на западном стратегическом направлении с целью прикрыть дальние подступы к Москве. Согласно плану Можайская линия обороны должна была включать 3 оборонительных полосы — главную и две тыловые, а также промежуточные и отсечные между ними. Можайская линия обороны простиралась с севера на юг от Волжского водохранилища до слияния р. Угра с Око.'

#Вопросы зала (Битва под Сталинградом)
qwestio_1 = '➖ Посмотрите на ордена на подложке №6. За что их могли дать?\n'\
       '\n'\
       '❓ 1. За оборону Ленинграда, за оборону Сталинграда, за взятие Будапешта, за победу над Германией\n' \
       '❓ 2. За оборону Ленинграда, за оборону Москвы, за битву под Берлином, за взятие Будапешта\n' \
       '❓ 3. За командирский дух, за просвещение взвода, за победу над Германией\n' \
       '❓ 4. За поднятие восстания, за побег из тыла врага, за оборону Сталинграда, за оборону Ленинграда\n'

qwestio_2 = '➖ Вдоль границ каких фронтов шла линия обороны на 19 ноября 1942 года?\n'\
       '\n'\
       '❓ 1. Воронежский, Сталинградский, Юго-Восточный фронты\n' \
       '❓ 2. Московский, Западный, Ленинградский фронты\n' \
       '❓ 3. Закавказский, Юго-Восточный, Московский фронты\n' \
       '❓ 4. Нижегородский, Сталинградский, Юго-Восточный фронты\n'

qwestio_3 = '➖ Посмотрите на письма, представленные на витрине. Какого числа было отправлено\написано первое письмо?\n'\
       '\n'\
       '❓ 1. 22.12.43 \n' \
       '❓ 2. 21.11.42\n' \
       '❓ 3. 20.10.41\n' \
       '❓ 4. 21.11.43\n'

qwestio_4 = '➖ Посмотрите на левую витрину. Что за форма на ней представлена? Какой стране принадлежит?\n'\
       '\n'\
       '❓ 1. Обмундирование  лыжника, СССР\n' \
       '❓ 2. Обмундирование альпиниста лыжника, СССР\n' \
       '❓ 3. Обмундирование альпиниста , СССР\n' \
       '❓ 4. Зимние обмундирование пехоты , СССР\n'

qwestio_5 = '➖ Повернитесь лицом к диораме, а потом посмотрите на правую стену. Какую скульптуру изобразил художник? Кто автор оригинала?\n'\
       '\n'\
       '❓ 1. Родина мать зовет, Скульптор Евгений Вучетич, архитектор Николай Никитин\n' \
       '❓ 2. Родина  зовет, Скульптор  Анатолий Вучетич, архитектор Анна Никитина\n' \
       '❓ 3. Родина мать , Скульптор Евгений Чистяков , архитектор Николай Никитин\n' \
       '❓ 4. Родина мать зовет, Скульптор Евгений Вучетич, архитектор Николай Кузьми\n'

qwestio_6 = '➖ Как вы думаете, почему Гитлеру было важно захватить Сталинград?\n'\
       '\n'\
       '❓ 1. В этом городе было крупнейшиее сборище танковых соединений \n' \
       '❓ 2. Город был красивым \n' \
       '❓ 3. Город на Волге был важнейшим транспортным и промышленным центром. Но не только это. Вероятно, фюрер видел в городе Сталина важнейший символ для советских людей\n' \
       '❓ 4. Город располагал нефтеными запасами \n'

qwestio_7 = '➖ Сколько бойцов насчитывала немецко-фашистская армия при битве под Сталинградом? Ответ поделите на 1000 и переведите в двоичную систему.\n'\
       '\n'\
       '❓ 1. 110000110\n' \
       '❓ 2. 101101010\n' \
       '❓ 3. 010101001\n' \
       '❓ 4. 110000100\n'

qwestio_8 = '➖ Когда началась “Битва под Сталинградом”?\n'\
       '\n'\
       'Введите ответ на этот вопрос в формате "ДД.М.ГГГГ":'

#Справки (Битва под Сталинградом)

refere_1 = ' ‼ Медалью «За оборону Сталинграда» награждались все участники обороны Сталинграда, принимавшие непосредственное участие в обороне.\n'\
'Медаль «За оборону Ленинграда» — одна из первых советских медалей военного времени государственная награда СССР для награждения защитников города Ленинград,\n'\
'Медалью «За взятие Будапешта» награждались непосредственные участники героического штурма и взятия Будапешта, а также организаторы и руководители боевых операций при взятии этого города.\n'\
'Медалью «За победу над Германией» награждались все военнослужащие и лица вольнонаемного штатного состава, служившие в период Великой Отечественной войны в рядах действующей армии.\n'\

refere_2 = ' ‼ 19 ноября 1942 г. началось контрнаступление Красной Армии под Сталинградом (операция «Уран») на трёх фронтах: Юго-Западном, Сталинградском и Донском с целью окружения и уничтожения вражеской группировки войск в районе города Сталинград.'

refere_3 = ' ‼ Письмо-треугольник представляло собой лист бумаги прямоугольной формы, загнутый сначала справа налево, а потом слева направо. Письмо проверялось цензурой. На наружной стороне писался адрес назначения и обратный, а также оставлялось чистое место. Послание писалось мельчайшим почерком. Зачастую она считалась похоронкой при смерти адресата.'

refere_4 = ' ‼ Отдельные горнострелковые отряды (ОГСО) — советские горнострелковые формирования, противостоящие во время Битвы за Кавказ немецким альпийским стрелкам. ОГСО комплектовались личным составом, обладающим высоким уровнем подготовленности для боевых действий в горной местности, снабжались специальным оружием, горным снаряжением и военной формой.'

refere_5 = ' ‼ Скульптура «Родина-мать зовет!» — композиционный центр памятника-ансамбля «Героям Сталинградской битвы» на Мамаевом кургане в Волгограде. Одна из самых высоких статуй мира, высочайшая статуя России (без постамента — самая высокая статуя в мире на момент постройки и в течение последующих 22 лет).'

refere_6 = ' ‼ Цели Гитлера в Сталинграде:\n'\
' - Захватить город, который носит имя вождя СССР, и подавить дух врага;\n'\
' - Совершить реванш после поражения под Москвой и поднять дух вермахта;\n'\
' - Отсечь Кавказ от всего СССР\n'\
' - Лишить Сталина бакинских нефтепромыслов;\n'\
' - Оставить Красную армию и советскую промышленность без топлива, зерна и иных жизненно важных ресурсов;\n'\
' - В итоге, победив Сталина в городе его имени, вовлечь в войну «сомневающихся» на тот момент Турцию и Японию.\n'\


refere_7 = ' ‼ За три недели наступления немецкие танки 4-й армии Гота подошли к Сталинграду с юга, 14-й танковый корпус — с севера, шесть дивизий 6-й армии Паулюса — с запада.\n'\
'14 октября пять немецких дивизий начали наступление при поддержке тысячи самолетов. К 11 ноября немцы вышли к Волге на участке в полкилометра. Но потеряли до половины личного состава.\n'\
'19 ноября в рамках операции «Уран» началось контрнаступление Красной армии. 23 ноября в районе Калача-на-Дону огромная фашистская группировка, пытавшаяся захватить Сталинград, была окружена.\n'\


refere_8 = ' ‼ 28 июня 1942 года началось наступление немецких войск. Первый этап операции прошел для них крайне успешно. В ходе битвы на большой излучине Дона советским войскам удалось задержать продвижение противника почти на три недели. Однако в двадцатых числах августа части 14-го танкового корпуса смогли форсировать Дон и стремительным броском вышли к окраинам Сталинграда. '

#Вопросы зала (Штурм Берлина)

question_1 = '➖ Найдите, кому принадлежит парадный китель, представленный в витрине.\n'\
       '\n'\
       '❓ 1. Жуков Георгий Константинович\n' \
       '❓ 2. Рокоссовский Константин Константинович\n'\
       '❓ 3. Берзарин Николай Эрастович\n' \
       '❓ 4. Будённый Семён Михайлович\n'

question_2 = '➖ Отыщите среди экспонатов бинокль 56Х30. Как вы думаете, какое из чисел дает понять степень его увеличения?\n'\
       '\n'\
       '❓ 1. Х8\n' \
       '❓ 2. Х106\n' \
       '❓ 3. Х2\n' \
       '❓ 4. X56\n'

question_3 = '➖ Найдите номер немецкого танка, нарисованного на одной из стен зала. определите его тип.\n'\
       '\n'\
       '❓ 1. 835 Panzerkampfwagen VI «Tiger»\n'\
       '❓ 2. 835 Sd.Kfz.184\n' \
       '❓ 3. 654  LT vz.35\n' \
       '❓ 4. 835 Leichttraktor\n'

question_4 = '➖ Сколько дивизий было разгромлено во время наступления на Берлин?\n'\
       '\n'\
       '❓ 1. 93\n'\
       '❓ 2. 90\n' \
       '❓ 3. 81\n' \
       '❓ 4. 56\n'

question_5 = '➖ Какое здание горит на диораме “Штурм Берлина”?\n'\
       '\n'\
       '❓ 1. Здание Генштаба\n'\
       '❓ 2. Рейхстаг\n' \
       '❓ 3. Бресткая крепость\n' \
       '❓ 4. Петропалавская крепость \n'

question_6 = '➖ Когда был подписан акт о капитуляции Германии?\n'\
       '\n'\
       '❓ 1. 8 мая 1945 года\n'\
       '❓ 2. 9 мая 1945 года\n' \
       '❓ 3. 1 сентября  1945 года\n' \
       '❓ 4. 24 июня 1941\n'

question_7 = '➖ В каком году было взятие войсками 1-го белорусского фронта Берлина?\n'\
       '\n'\
       '❓ 1. 03.05.1944\n' \
       '❓ 2. 05.02.1945\n' \
       '❓ 3. 31.05.1945\n' \
       '❓ 4. 02.05.1945\n'

question_8 = '➖ Кто является автором диорамы “Штурм Берлина”?\n'\
       '\n'\
       '❓ 1. Вениамин Михайлович Сибирский\n'\
       '❓ 2. Евгений Александрович Суворов\n' \
       '❓ 3. Геннадий Иванович Заразин\n' \
       '❓ 4. Эдуард Иванович Секереш\n'

question_9 = '➖ В 700-километровой полосе от Балтийского моря до Судетских гор было сражение. С какого по какое число оно шло?\n'\
       '\n'\
       '❓ 1. С 16 апреля по 8 мая\n'\
       '❓ 2. С 10 апреля по 7 августа \n' \
       '❓ 3. С 31 января по 1 сентября\n' \
       '❓ 4. С 14 сентября по 9 января\n'

question_10 = '➖ Среди музейных экспонатов найдите полковую пушку 1943 года и назовите ее калибр.\n'\
       '\n'\
       '❓ 1. 81 см\n' \
       '❓ 2. 81 мм\n'\
       '❓ 3. 45 м\n' \
       '❓ 4. 71 мм\n'

question_11 = '➖ Как вы думаете, почему художник изобразил главную сцену “передачи знамени” не затянутой дымом?\n'\
       '\n'\
       '❓ 1. Автор желал подчеркнуть главные черты, запечатленных людей\n' \
       '❓ 2. Художник хотел показать уверенность в победе. Также эта сцена является самой главной и яркой в диораме.\n'\
       '❓ 3. В этом месте изначально не должно было быть тумана\n' \
       '❓ 4. Художник тем самым пытался передать уверенность действующих лиц\n'

question_12 = '➖ Что за здание расположено в правой части диорамы ?\n'\
       '\n'\
       'Введите ответ на вопрос с маленькой буквы:'

l1 = ['а', 'б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш', 'щ', 'ъ', 'ы','ь','э', 'ю', 'я']
l2 = ['а', 'б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш', 'щ', 'ъ', 'ы','ь','э', 'ю', 'я']
l3 = ['а', 'б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш', 'щ', 'ъ', 'ы','ь','э', 'ю', 'я']
l4 = ['а', 'б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш', 'щ', 'ъ', 'ы','ь','э', 'ю', 'я']
l5 = ['а', 'б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш', 'щ', 'ъ', 'ы','ь','э', 'ю', 'я']
l6 = ['а', 'б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш', 'щ', 'ъ', 'ы','ь','э', 'ю', 'я']
l7 = ['а', 'б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш', 'щ', 'ъ', 'ы','ь','э', 'ю', 'я']
l8 = ['а', 'б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш', 'щ', 'ъ', 'ы','ь','э', 'ю', 'я']

#Справки зала (Штурм Берлина)

r_1 = ' ‼ Самый простой способ отличить военные формы СССР и третьего рейха, это по цвету. Немецкие войска носили одежду серого (Вермахт) и чёрного (СС или штабные офицеры) цвета. У них были приплюснутые каски и множество ремней. Наши войска в основном одевались в зелёные тона, а офицерский состав имел штаны синего цвета, а так же красные прошивки на погонах и верхней одежде.'
r_2 = ' ‼ Оптика и вооружение трудно разделимые понятия. В годы Великой Отечественной войны оптическая промышленность сыграла огромную роль, удовлетворяя запросы армии и флота. Оптическими приборами оснащали орудия, самолёты, танки, на фронт было поставлено огромное количество биноклей и прицелов для снайперских винтовок.'
r_3 = ' ‼ Танковые сражения были неотъемлемой частью ВОВ. Ни в какой другой войне танки не играли такой роли. Фашистская военная машина создала поистине устрашающие и совершенные на тот момент танки. '
r_4 = ' ‼ Берлинская операция делится на три этапа:\n'\
       '\n'\
       '1) прорыв вражеской обороне на реках Одер и Нейсе.\n'\
       '2) развитие наступления, расчленение берлинской группировки вермахта на три части, создание районов окружения в Берлине и юго-восточнее германской столицы.\n'\
       '3) уничтожение немецких войск в Западной Померании, штурм Берлина, ликвидация «котлов» и выход советских армий на широком фронте к Эльбе, где произошла встреча с союзниками.\n'\
       '\n'\
       'Битва завершилась полной победой Красной Армии. Берлинская группировка вермахта была разгромлена, рассеяна и пленена. Советские войска полностью разгромили 93 дивизии и 11 бригад противника, около 400 тыс. человек было убито, около 450 тыс. человек взято в плен.'

r_5 = ' ‼ В 1923 году — преобразован в РВС СССР.\n'\
'22 сентября 1935 Штаб РККА был переименован в Генеральный штаб РККА.\n'\
'В годы Великой Отечественной войны 1941—45 Генеральный штаб являлся основным органом Ставки Верховного Главнокомандования по стратегическому планированию и руководству вооруженными силами на фронтах.'

r_6 = ' ‼ Акт о капитуляции подписывался дважды. В первый раз акт о безоговорочной капитуляции Германии был подписан 7 мая 1945 года в Реймсе.\n'\
'От имени германского Верховного командования его подписал генерал-полковник Альфред Йодль, от англо-американской стороны – генерал-лейтенант армии США Уолтер Беделл Смит, от СССР – генерал-майор Иван Суслопаров. Капитуляция нацистской Германии вступала в силу 8 мая в 23:01 по среднеевропейскому времени (9 мая в 01:01 по московскому времени).'

r_7 = ' ‼ 1-й Белорусский фронт — формирование РККА, один из фронтов Красной Армии, на заключительном этапе Великой Отечественной войны. Образован 24 февраля 1944, упразднён 5 апреля, но уже 16 апреля восстановле до конца войны.'
r_8 = ' ‼ Родился в 1936 году в городе Бузулук.\n'\
'С 1951 по 1956 годы В. М. Сибирский обучался в Московском областном художественном педагогическом училище изобразительных искусств. \n'\
'С 1965 года В. М. Сибирский помимо творческой деятельности начал заниматься и педагогической работой.\n'\
'С 1964 года В. М. Сибирский является членом Союза художников СССР. '

r_9 = ' ‼ Берлинская операция стала одной из последних стратегических операций Красной Армии в Европе. Советские войска заняли столицу Германии и поставили победную точку в Великой Отечественной войне и Второй мировой войне на Европейском театре военных действий.'
r_10 = ' ‼ Калибр  — диаметр, расстояние между противоположными полями нарезов; одна из основных величин, определяющих мощность огнестрельного оружия.'
r_11 = ' ‼ Знамя Победы — штурмовой флаг 150-й ордена Кутузова II степени Идрицкой стрелковой дивизии, водруженный 1 мая 1945 года на крыше здания рейхстага военнослужащими Красной Армии. Это было четвёртое по счёту знамя из установленных на крыше здания. Первые три знамени были уничтожены.'
r_12 = ' ‼ Рейхстаг — историческое здание в Берлине, где в 1894—1933 годах заседал одноимённый государственный орган Германии — рейхстаг Германской империи и рейхстаг Веймарской республики, находится на площади Республики. В 1945 году в Советском Союзе здание германского парламента было объявлено главным символом гитлеровской Германии. И.В. Сталин приказал водрузить на нём Знамя Победы.'

#Вопросы зала (Блокада Ленинграда)
que_1 = ' ➖ Вы зашли в зал, справа от вас находятся объявления. Соотнесите заголовок с содержанием газет.\n'\
       '\n'\
       'A) “Городской театр”\n'\
       'Б) “Филармония 12”\n'\
       'В) “Большой зал Филармонии 7”\n'\
       'Г)  “Большой зал Филармонии, вечер балета”\n'\
       '\n'\
       '1) Концерт фронтовых бригад театр краснознаменного Балтийского флота\n'\
       '2) Русские люди, Евгений Онегин, фронт\n'\
       '3) О.Г.Иордан , Р.Г.Гербек\n'\
       '4) Бетховен\n'\
       '\n'\
       'Выберите нужную комбинацию:\n'\
       '\n'\
       ' ❓ 1. А-3, Б-1, В-2, Г-4\n'\
       ' ❓ 2. А-2, Б-4, В-1, Г-3\n'\
       ' ❓ 3. А-2, Б-1, В-3, Г-4\n'\
       ' ❓ 4. А-1, Б-2, В-3, Г-4\n'\

que_2 = '➖ Посмотрите на диораму. На какой реке происходят события?\n'\
       '\n'\
       '❓ 1. Нева\n' \
       '❓ 2. Черная\n'\
       '❓ 3. Екатерингофка\n'\
       '❓ 4. Красненькая\n'

que_3 = '➖ Поднимите глаза под потолок. В каком порядке располагаются слова?\n'\
       '\n'\
       '❓ 1. “Слава и тебе, великий город. Сливший воедино фронт и тыл, в небывалых трудностях который выстоял, остался, победил!\n' \
       '❓ 2. “Слава и тебе, великий город. Сливший воедино фронт и тыл, в небывалых трудностях который выстоял, сражался, победил!”\n'\
       '❓ 3. “Слава и тебе, родимый город. Сливший воедино фронт и тыл, в бывалых трудностях который выстоял, сражался, победил!”\n'\
       '❓ 4. “Слава и тебе, великий город. Сливший воедино фронт и тыл, в бывалых трудностях который выстоял, сражался, победил!\n'

que_4 = '➖ Какое здание видно в левой части диорамы?\n'\
       '\n'\
       '❓ 1. Исаакиевский собор\n' \
       '❓ 2. Петропавловский собор\n'\
       '❓ 3. Спас на Крови\n'\
       '❓ 4. Никольский морской собор\n'

que_5 = '➖ Какое количество фронтов принимало участие в сражениях за Ленинград?\n'\
       '\n'\
       '❓ 1. 5\n' \
       '❓ 2. 22\n'\
       '❓ 3. 4\n'\
       '❓ 4. 3\n'

que_6 = '➖ Сколько дней продолжалась блокада?\n'\
       '\n'\
       '❓ 1. 872 дня\n' \
       '❓ 2. 862 дня\n'\
       '❓ 3. 789 дней\n'\
       '❓ 4. 95 дней\n'

que_7 = '➖ По какому озеру привозили боеприпасы и еду в блокадный Ленинград? При помощи таблицы кодов кириллицы запишите ответ в десятичной кодировке UNICODE\n'\
       '\n'\
       'Ответ запишите в формате "... ... ... ..."'

#Справки для зала (Блокада Ленинграда)

ref_1 = ' ‼ В городе, несмотря на блокаду, продолжалась культурная, интеллектуальная жизнь. В первую блокадную зиму продолжали работать несколько библиотек. Продолжало работать Ленинградское радио. В августе 1941 года из города были эвакуированы практически все театральные коллективы. Представления продолжались во время артиллерийских обстрелов, во время заморозков, иногда актеры умирали во время представлени. 18 октября 1942 года открылся Городской театр, получивший название «Блокадный».  В августе 1942 года была вновь открыта городская филармония, где стали регулярно исполнять классическую музыку.'

ref_2 = ' ‼ Нева — река, протекающая по территории Ленинградской области и Санкт-Петербурга, соединяющая Ладожское озеро с Невской губой Финского залива Балтийского моря. Нева была не только линией фронта блокадного Ленинграда — она обеспечивала осажденный город водами Ладожского озера.'

ref_3 = ' ‼ Военная блокада города Ленинграда немецкими и финскими войсками и их союзниками во время Великой Отечественной войны. Длилась с 8 сентября 1941 года по 27 января 1944 года  — блокада продолжалась 872 дня, в ряде источников 871 день.'

ref_4 = ' ‼ Во время Великой Отечественной войны собор пострадал от бомбёжек, артобстрела, холода и сырости; на стенах и колоннах местами сохранены следы от снарядов. В соборе во время блокады хранились экспонаты музеев из пригородов Ленинграда, а также Музея истории города и Летнего дворца Петра I.'

ref_5 = ' ‼ Северный фронт - оборона Кольского полуострова и северных берегов Финского залива.\n'\
       'Волховский фронт - прорыв блокады Ленинграда и соединение с войсками Ленинградского фронта\n'\
       'Корельский и 2-ой Прибалтийский - перед этим фронтом не было каких-то особых задач, он оборонял Пушкинские Горы, Идрицу, а в дальнейшем вели бои по уничтожению курляндской группировки противника.\n'\
       'Краснознаменский Балтийский фронт - содействие войскам Северо-Западного и Северного фронтов на приморских направлениях.\n'\
       'Ладожская и Онежская флотилия - поддержка наступающих по берегам Ладожского озера советских войск и борьба с финскими военными судами.'

ref_6 = ' ‼ На подступах к Ленинграду фашистская армия пыталась занять Пулковские высоты. Но яростное сопротивление советской армии не позволило фашистам занять эту выгодную точку. Героические действия советской обороны лишили фашистские войска значительной части боеприпасов, танков и солдат. Дальнейшее наступление на город было прекращено.'

ref_7 = ' ‼ Особое значение в обеспечении блокадного города продовольствием имела Дорога жизни. Это единственная транспортная магистраль через Ладожское озеро. В периоды навигации — по воде, зимой — по льду, она связывала блокадный Ленинград со страной.'

#Вопросы для зала (Курская битва)
qwes_1 = '➖ На какую из перечисленых танковых дивизий СС не возлагались большие надежды Вермахта?\n'\
       '\n'\
       '❓ 1. "Мертвая голова"\n' \
       '❓ 2. "Кампф"\n'\
       '❓ 3. "Адольф Гитлер"\n'\
       '❓ 4. "Рейх"\n'

qwes_2 = '➖ Каким событием завершилась Курская битва?\n'\
       '\n'\
       '❓ 1. Взятием Харькова\n' \
       '❓ 2. Битвой под Прохоровкой\n'\
       '❓ 3. Битвой под Нефедовым\n'\
       '❓ 4. Взятием Киева\n'

qwes_3 = '➖ Какие события положены в основу сюжета диорамы “Курская битва”?\n'\
       '\n'\
       '❓ 1. Разгром немецко-фашистских войск на Курской дуге\n' \
       '❓ 2. Поражение армии советов на Курской дуге\n'\
       '❓ 3. Курск и прилегающие территории до войны\n'\
       '❓ 4. Разгром союзных армий на Курской дуге\n'

qwes_4 = '➖ Рассмотрите стены зала и найдите людей-офицеров, находящихся перед картой. Назовите самое высокое звание среди них.\n'\
       '\n'\
       '❓ 1. Генерал СССР\n' \
       '❓ 2. Половник СССР\n'\
       '❓ 3. Маршал Третьего Рейха\n'\
       '❓ 4. Маршал СССР\n'

qwes_5 = '➖ Сколько танков насчитывалось с обеих сторон?\n'\
       '\n'\
       'Введите число, кол-во танков:'

qwes_6 = '➖ Как в Германии называли данную операцию?\n'\
       '\n'\
       'Ответ запишите используя Шифр Цезаря заглавными буквами со сдвигом на 3\n'

#Справки для зала (Курская битва)

refe_1 = ' ‼ Из всех дивизий, на которые возлагались большие надежды, дивизия  “Адольф Гитлер” является самой интересной, так как это элитное формирование создано на базе личной охраны Адольфа Гитлера. До начала боевых действий подчинялось лично диктатору. Начиная с 1943 года формирование действовало на самых трудных участках и было семь раз переброшено между восточным и западным фронтами.'

refe_2 = ' ‼ Взятию Харькова придавалось очень большое значение. В составе войск фронтов имелось три общевойсковые, две танковые и одна воздушная армии, две армии имелись в резерве Ставки.'

refe_3 = ' ‼ Это совокупность стратегических оборонительной и наступательных операций Красной армии в Великой Отечественной войне с целью сорвать крупное наступление сил вермахта и разгромить его стратегическую группировку.'

refe_4 = ' ‼ Среди стен диорамы присутствует большое количество разных по званию солдат. Самые высокие из них : Маршал, генерал армии, генерал-полковник, генерал-лейтенант. Они все запечатлены на фоне плана контрнаступления советских войск.'

refe_5 = ' ‼ С советской стороны, в этой грандиозной серии сражений принимали участие 2758 танков и самоходок; с немецкой – 3444.\n'\
       'Среди танков СССР были Т-34, КВ-1, очень маленькое количество танков КВ-2 и их подвиды с различными модификациями.\n' \
       'Силы вермахта имели в распоряжении танки Pz.Kpfw. III, PzKpfw IV, PzKpfw V «Пантера» и самый известный немецкий танк Pz Kpfw VI «Тигр»'

refe_6 = ' ‼ Гитлеровское командование рассчитывало взять реванш за своё поражение под Сталинградом. Победа над Красной Армией могла привести к последующему наступлению германских войск на юго-восточном или северо‑восточном направлениях, обеспечить надежную оборону немецких позиций на остальных участках фронта, заставить союзников СССР отказаться от своих планов высадки войск во Франции.'


# import sqlite3
# import telebot
#
# bot = telebot.TeleBot('5039673735:AAG9T15Psch35kRvOZoOFuHOMNVTezmi2FY')
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Добро пожаловать.')
#
# connection = sqlite3.connect("C:\\Users\\artem\\OneDrive\\Рабочий стол\\bot.project\\people.db", check_same_thread=False),
# cursor = connection.cursor()
#
#
# def db_table_val(user_id: int, user_name: str):
#     cursor.execute('INSERT INTO test (user_id, user_name) VALUES (?, ?, ?, ?)',
#                    (user_id, user_name))
#     connection.commit()
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Добро пожаловать')
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
#
#         us_id = message.from_user.id
#         us_name = message.from_user.first_name
#
#         db_table_val(user_id=us_id, user_name=us_name)
#
#
# bot.polling(none_stop=True)

# import sqlite3
# import telebot
# from telebot import types
#
# bot = telebot.TeleBot("5090683807:AAFTgXnhn5qDpqOv9IgjEuAeSzMe6eVPViE")
#
# conn = sqlite3.connect('C:\\Users\\artem\\OneDrive\\Рабочий стол\\bot.project\\people.db', check_same_thread=False)
# cursor = conn.cursor()
#
#
# def db_table_val(user_id: int, user_class: int):
#     cursor.execute('INSERT INTO io (user_id, user_class) VALUES (?, ?)',
#                    (user_id, user_class))
#     conn.commit()
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Добро пожаловать')
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton("Вывести случайную цитату Ленина")
#     markup.add(button1)
#     if message.text.lower() == 'привет':
#
#
#         bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!', reply_markup=markup)
#
#         us_id = message.from_user.id
#         us_name = message.message.chat.id
#
#         db_table_val(user_id=us_id, user_class=us_name)
#
#
# bot.polling(none_stop=True)