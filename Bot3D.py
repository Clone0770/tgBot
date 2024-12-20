import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

API_TOKEN = '7887163588:AAFi04WbXLc_Uf2B47UxhYrZbmIWoHI3d4I'

bot = telebot.TeleBot(API_TOKEN)

# Главное меню
def get_main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("📚 Список ПО для 3D-моделирования", callback_data='software_list'),
        InlineKeyboardButton("📚 Список ПО для печати 3D-моделей", callback_data='software_list_print'),
        InlineKeyboardButton("📚 Официальные сайты для скачивания ПО", callback_data='official_sites'),
        InlineKeyboardButton("📚 Гайд: Как начать изучение", callback_data='guide_start'),
        InlineKeyboardButton("📚 Популярные ошибки и их решения", callback_data='common_mistakes'),
        InlineKeyboardButton("📚 Советы по постобработке", callback_data='post_processing'),
        InlineKeyboardButton("📚 Обратная связь", callback_data='feedback')
    ]
    markup.add(*buttons)
    return markup

# Хэндлер команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот-помощник по 3D-моделированию. Выбери интересующий раздел:", reply_markup=get_main_menu())

# Хэндлеры для кнопок
@bot.callback_query_handler(func=lambda call: call.data == 'software_list')
def software_list(call: CallbackQuery):
    text = """\
 **Список рекомендуемого ПО для 3D-моделирования**:

1 - **Blender** — Подойдёт для создания игровых моделей, рендеринга и анимации.

    ➕Плюсы программы:
    Огромное число инструментов
    Полностью бесплатно
    Разные движки рендера
    
    ➖Минусы программы:
    Не подходит для четрежей
    Может показаться сложным на первое время
    

2 - **Компас 3D** — для создания точных моделей и четрежей.

    ➕Плюсы программы:
    Полностью русский интерфейс
    Большое количество инструментов
    Наличие бесплатной студенческой версии
    Очень низкая цена
    
    ➖Минусы программы:
    Нужен относительно мощный ПК
    Сложна в освоении на профессиональном уровне


3 - **SolidWorks** — предназначена для больштх производств.

    ➕Плюсы программы:
    Простота в освоении
    Наличие русского интерфейса
    Большое сообщество людей, использующих SolidWorks
    Широко распространена в России
    
    ➖Минусы программы:
    Отсутствие версии для частного использования
    Загроможденный интерфейс


4 - **Tinkercad** — для создания самых простых моделей, работает по интернету.

    ➕Плюсы программы:
    Простота в освоении
    Не нужно устанавливать на ПК
    Доступ к моделям с любого устройства
    
    ➖Минусы программы:
    Невозможность работать без интернета
    Каждый отдельный проект нужно скачивать
    Ограниченное число инструментов
    
5 - **3ds Max** — для создания 3D-моделей и рендера изображений.

    ➕Плюсы программы:
    Огромный функционал
    Возможность создания рендеров
    
    ➖Минусы программы:
    Необходим мощный ПК
    Большая цена
    Сложна в освоении
    Отсутствует русский язык
    """
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_main_menu(), parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data == 'software_list_print')
def software_list_print(call: CallbackQuery):
    text = """\
     **Список рекомендуемого ПО для 3D-печати**:

1 - **Ultimaker Cura** — Стандартный выбор для новичков, имеет простой интерфейс
    
    ➕Плюсы программы:
    Простота настроек
    Регулярные обновления
    Продвинутый режим предпросмотра
    
    ➖Минусы программы:
    Долгий запуск на любом компьютере
    Малоинформативная консоль управления принтером
    

2 - **Prusa Slic3r** — Гибкая настройка толщины слоя и множество доступных принтеров.
    
    ➕Плюсы программы:
    Продвинутая система профилей
    Сверхбыстрый запуск
    Удобная работа с двухэкструдерными принтерами
    
    ➖Минусы программы:
    Отсутствие управления принтером через провод
    Относительно малое количество настроек
    
    
3 - **MatterControl 2.0** — имеет в себе слайсер и редактирование stl файлов одновременно.
    
    ➕Плюсы программы:
    Встроенный редактор моделей
    Понятный интерфейс
    Есть библиотека профилей для популярных принтеров
    
    ➖Минусы программы:
    Мало настроек слайсинга
    Отсутствие поддержки русского языка
    """
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_main_menu(), parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data == 'official_sites')
def official_sites(call: CallbackQuery):
    text = """\
➕ **Официальные сайты для скачивания ПО**:

1 - [Blender](https://www.blender.org/download/)

2 - [Компас 3D](https://kompas.ru)

3 - [SolidWorks](https://www.solidworks.com)

4 - [Tinkercad](https://www.tinkercad.com)

5 - [UltiMaker Cura](https://ultimaker.com/software/ultimaker-cura/)

6 - [Prusa Slic3r](https://www.prusa3d.com/page/prusaslicer_424/)

7 - [MatterControl 2.0](https://www.matterhackers.com/store/l/mattercontrol/sk/MKZGTDW6)
    """
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == 'guide_start')
def guide_start(call: CallbackQuery):
    text = """\
➕ **Гайд: Как начать изучение 3D-моделирования**:

1. Определи цель и направление
Выясни, для чего ты хочешь изучать 3D-моделирование:

- Создание персонажей для игр или анимации
- Архитектурная визуализация
- Визуальные эффекты (VFX)
- Дизайн предметов или интерьеров
- От цели зависит выбор программного обеспечения и методов работы.

2. Выбери подходящее программное обеспечение
Начни с одной из популярных программ для 3D-моделирования:

- Blender (бесплатная и многофункциональная программа)
- 3ds Max (для архитектурной визуализации и игр)
- Maya (для анимации и VFX)
- ZBrush (цифровая скульптура и персонажи)
- Cinema 4D (для анимации и моушн-дизайна)

3. Изучи базовые понятия 3D-моделирования:
- полигоны
- меши
- текстуры.

5. Следуй обучающим курсам и туториалам
Начни с простых видеокурсов на YouTube или онлайн-платформах:

6. Практикуйся на простых проектах
Выполни небольшие проекты для закрепления навыков:

- Создай чашку, стул или простой дом
- Попробуй создать свой первый персонаж
- Сделай простую анимацию, например, движение шара

7. Изучай материалы по освещению и текстурам.
- Научись добавлять текстуры, создавать материалы и UV-развёртки

8. Научись рендерить сцены
Изучи, как делать финальные изображения и анимации с помощью рендеринга:

- Настрой освещение и камеры
- Используй рендеры, такие как Cycles (Blender) или Arnold (Maya)

9. Осваивай дополнительные инструменты и плагины
После базового освоения программы начни изучать расширенные инструменты:

- Скульптинг
- Физическая симуляция (дыма, жидкости)
- Сторонние плагины для улучшения работы
    """
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == 'common_mistakes')
def common_mistakes(call: CallbackQuery):
    text = """\
➕ **Популярные ошибки и их решения**:

1. Слишком высокая или низкая детализация
Ошибка:
Создание моделей с избыточным количеством полигонов (перегруженная геометрия) или, наоборот, слишком низкая детализация, что делает модель нереалистичной.

Решение:

- Для игр и реального времени: Используй Low-Poly для оптимизации производительности, а детали добавляй через нормальные карты.
- Для анимаций и рендеров: Сбалансируй количество полигонов в зависимости от того, насколько близко к камере будет объект.
- Используй Subdivision Surface для управления детализацией.

2. Неправильная топология
Ошибка:
Модель с хаотичной сеткой (треугольники, N-угольники вместо правильных квадов). Это приводит к проблемам при анимации и текстурировании.

Решение:

- Используй четырёхугольники (quads) вместо треугольников и N-угольников.
- Применяй Loop Cuts для создания плавных линий в сетке.
- Следи за правильным направлением лупов для удобства при риггинге и анимации.


3. Проблемы с UV-развёрткой
Ошибка:
UV-развёртка с растянутыми или перекрывающимися UV-островками приводит к неправильному отображению текстур.

Решение:

- Делай UV-развёртку с минимальным растяжением и искажением.
- Используй функции автоматического UV-unwrap (например, Smart UV в Blender), но корректируй вручную.
- Размещай UV-островки так, чтобы они равномерно заполняли пространство UV-карты.


4. Неправильное масштабирование моделей
Ошибка:
Создание объектов в несоответствующем масштабе приводит к трудностям в анимации и сценах.

Решение:

- Убедись, что модель имеет реальные размеры (например, человек должен быть около 1,8 м).
- Используй единицы измерения программы (метры, сантиметры) и применяй Apply Scale (в Blender: Ctrl + A → Scale).


5. Неправильное освещение
Ошибка:
Использование слишком яркого или тусклого освещения делает сцену плоской или перенасыщенной.

Решение:

- Применяй три ключевых источника света: ключевой, заполняющий и контровой.
- Используй HDRI-карты для реалистичного окружения.
- Экспериментируй с интенсивностью и цветом света для создания атмосферы.


6. Проблемы с нормалями
Ошибка:
Неправильное направление нормалей приводит к черным или прозрачным поверхностям на рендере.

Решение:

- Включи отображение нормалей в программе.
- Исправь их направлением через Recalculate Normals (в Blender: Shift + N).
- Убедись, что все внешние поверхности направлены наружу.
    """
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == 'feedback')
def feedback(call: CallbackQuery):
    text = """\
✉️ **Обратная связь**:

По всем возникающим вопросам, можно писать сюда: @clone456
    """
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == 'post_processing')
def post_processing(call: CallbackQuery):
    text = """\
➕ **Советы по постобработке**:

1. Используй композитинг для финальных штрихов
Композитинг позволяет комбинировать разные рендер-пассы и добавлять эффекты. В таких программах, как Blender, After Effects, Nuke, или Photoshop, можно работать с отдельными слоями изображения.

Основные рендер-пассы:
- Ambient Occlusion для усиления теней в углах.
- Depth Pass для создания эффекта глубины резкости.
- Normal Map для точного освещения и коррекции деталей.
- Diffuse, Specular, и Shadow Passes для тонкой настройки света и отражений.


2. Добавляй глубину резкости (Depth of Field)
- Создавай размытые фоны для фокусировки внимания на основном объекте.
- Используй Z-pass для маскировки области фокуса в композитинге.
- В Photoshop или After Effects можно применять фильтры размытия, такие как Lens Blur или Gaussian Blur.


3. Цветокоррекция и градация цвета
Правильная цветокоррекция может изменить настроение изображения.
- Улучшай контраст и баланс белого.
- Используй кривые (Curves) и уровни (Levels) для тонкой настройки теней, средних тонов и светов.
- Применяй цветовые LUT-файлы (Look-Up Tables) для имитации киношного стиля.


4. Добавляй эффекты линзы
Эффекты камеры могут сделать изображение реалистичнее:
- Bloom/Glare: Добавляет мягкое свечение вокруг ярких объектов (например, ламп или солнца).
- Lens Flare: Создаёт блики и ореолы света при попадании яркого источника в камеру.
- Chromatic Aberration: Лёгкое расслоение цветов по краям изображения для имитации несовершенства линз.


5. Добавь виньетирование
- Лёгкое затемнение углов изображения помогает направить взгляд зрителя к центру композиции.
- В Photoshop можно добавить через фильтр Lens Correction → Custom → Vignette.

    """
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_main_menu(), parse_mode="Markdown")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
