# Google Business Profile — состояние

## Карточка

| Параметр | Значение |
|---|---|
| Название | Ma Permanent Studios |
| Рейтинг | 5.0 ★, 37 отзывов |
| Взаимодействий | 351 |
| Просмотров/мес | 1639 |
| Основная категория | Permanent make-up clinic |

Управление ведётся через панель, встроенную в выдачу поиска (не через отдельный дашборд).

## Услуги (после правок 13 сентября)

| Услуга | Цена | Тип |
|---|---|---|
| Lash tattooing | From $380 | стандартный Google |
| Lip blushing | From $440 | стандартный |
| Permanent eyeliner | From $550 | стандартный |
| Permanent makeup touch-ups | From $150 | стандартный |
| Powder brow styling | $440 | `job_type_id:powder_brow` |
| Scalp micropigmentation | From $1,100 | стандартный |
| Scar camouflage | From $200 | `job_type_id:scar_camouflage` |
| Eyebrow tinting | From $60 | ⚠️ на сайте такой услуги нет |
| Korean lash lift | $90 | кастомная |
| 3D Areola Tattoo | From $650 | `0c7f8300-466b-411e-a77e-60bc0cb165fc` |
| Lash extensions | From $130 | кастомная |
| Under-Eye Dark Circle Camouflage | $420 | кастомная |
| **Nano & Combo Brows** | $480 | `5dd6cb80-9dd4-4fd4-9528-a30ce63c5d45` |
| Combo Brows | $480 | `ff54a972-0f75-4c9e-8398-c58090149730` ⚠️ дубль, см. ниже |
| Ombre Lips | $440 | `bbce5804-8fd9-4661-9e4b-f4b89504971d` |
| Angel Lips Berry Kiss | $440 | `cb5250ad-82bc-432e-90c8-d3dd49130ab9` |
| Lipstick Effect Lips | $440 | `d46f4672-0715-4753-9869-7f36fe9b84a6` |

**Удалены 13 сентября:** `job_type_id:eyebrows` (Eyebrows, From $440) и `job_type_id:eyebrow_tattooing` (Eyebrow tattooing, From $440) — дублировали Powder/Nano/Combo Brows.

**Доступные, но не добавленные стандартные типы:** BOTOX treatments, Dermaplaning, Eyebrow embroidery, Eyelash enhancements, Eyeliners, Hair extensions, Lash perming, Lip fillers, Medical micropigmentation, Microblading, Microshading, Nanoblading, Nipple coloring, Ombre eyebrow styling, Permanent lip makeup.

## Правка Nano & Combo Brows (13 сентября)

Услуга `5dd6cb80-9dd4-4fd4-9528-a30ce63c5d45`, раздел `permanent_make_up_clinic`.

**Название:** «Nano Brows» → «Nano & Combo Brows»
**Цена:** $480 фикс. — **не менялась**

**Описание было** (287/300):
> Nano Brows (Nano Blading / Nano Brading) is a modern hair-stroke technique using an ultra-fine needle for crisp, natural-looking eyebrow strokes. A refined alternative to microblading, ideal for anyone who wants soft, realistic brows with less trauma to the skin. Results last 1-2 years.

**Описание стало** (238/300):
> Nano Brows is a modern hair-stroke technique using an ultra-fine needle for crisp, natural brows — a low-trauma alternative to microblading. We also offer Combo Brows: hair-strokes blended with soft powder shading. Results last 1-2 years.

Alex явно потребовал сохранить формулировку «modern technique» — в лимит 300 символов вместе с упоминанием combo старый текст целиком не помещался, поэтому сокращены второстепенные части (расшифровка «Nano Blading / Nano Brading», развёрнутое «ideal for anyone who wants…»).

Подтверждено тостом: «Сведения об услугах отредактированы. Изменения скоро будут опубликованы».

**Карточка остаётся на английском.** Русские названия в интерфейсе — автоперевод стандартных типов Google (см. раздел про ложную тревогу ниже). Клиент в LA видит английский; переводить кастомные услуги на русский смысла нет.

### ⚠️ Открыто: дубль «Combo Brows»

Отдельная услуга **«Combo Brows» ($480)**, id `ff54a972-0f75-4c9e-8398-c58090149730`, осталась в карточке без изменений — не удалялась и не редактировалась, решения по ней не принималось.

Теперь это дубль: combo описана внутри «Nano & Combo Brows». Варианты — удалить дубль либо оставить как отдельную точку входа под запрос «combo brows». Команды от Alex нет.

## Решение по позиционированию

Alex: «Я хочу, чтобы на этой странице был перманентный макияж». Карточка должна содержать **только PMU**.
Кандидаты на удаление: Eyebrow tinting $60, Korean lash lift $90, Lash extensions $130.
Принцип согласован, **команда на удаление по каждой позиции не дана**.

## Закрытая ложная тревога — язык карточки

Русские названия услуг в интерфейсе — стандартные типы из справочника Google, автоматически переводимые под язык посетителя. Клиент в LA видит всё по-английски (проверено через `&hl=en`). Пункт «привести услуги к единому языку» снят как несуществующая проблема.

## 15 задач по GBP

Исходный список хранится в Reminders, list «Напомнить!!!!», listId `D7F007AD-D6BA-44EB-BFFE-69A828727E7B`.

| # | Задача | Статус | Кто |
|---|---|---|---|
| 1 | Подключить Wix к карточке через «Import Existing Profile» | ⏳ | Alex |
| 2 | Удалить дублирующую карточку «MA Permanent Makeup Studio» | ⏳ | Alex |
| 3 | Убрать третью карточку «Ma permanent studios» | ⏳ | Alex |
| 4 | Утечка текста в описании Nano Brows | ✅ | — |
| 5 | Утечка текста в публикации ~2-недельной давности | ✅ | — |
| 6 | Порядок в списке услуг | ⚠️ частично | Claude |
| 7 | Добавить категории Beauty salon и Eyebrow bar | ⏳ | Alex |
| 8 | Ответить на ≥5 отзывов (старейший 18 недель) | ⏳ | Claude (черновики) |
| 9 | Решить вопрос с названием карточки | ⏳ | Alex |
| 10 | Заполнить пустые атрибуты профиля | ⏳ ждёт данных | Claude |
| 11 | Привязать Google Ads к профилю | ⏳ | Alex |
| 12 | Заполнить Q&A (8–10 вопросов с FAQ сайта) | ⏳ | Claude |
| 13 | Упомянуть район живой фразой (необязательно) | ⏳ | Claude |
| 14 | Фото интерьера и мастеров, удалить 1 отклонённое | ⏳ | Alex |
| 15 | 1 октября: Nano & Combo Brows $480 → $550 | 🔴 дедлайн | оба |

**Неотвеченные отзывы:** Мария (powder brows), Vika_662, Vasilisa Troy, Diana, Svetlana Romanchuk.

**Атрибуты — нужны факты от Alex, не угадывать:** вход для колясок, парковка (уличная/своя), приём только по записи, туалет для клиентов, Wi-Fi, оплата картой, women-owned, LGBTQ+ friendly.

**Про пункт 13:** перечисление районов = keyword stuffing, на ранжирование не влияет. Только одна живая фраза.

## Влияние GBP (разобрано)

Сам по себе приток даёт слабый. **Категории** — единственный пункт с заметным влиянием на выдачу. Заполненный профиль даёт доверие ×2.7, +70% к вероятности визита, +50% к покупке.

## Публикации в профиле

- «Beautiful Ombré Powder Brows ✨…»
- «Nano Brows Special — $480»
- «Men's Permanent Makeup: Natural, Masculine Brows» (с кнопкой Book)
- «Natural Lip Blush in Los Angeles 💋» — id `965250967653855412`, правка внесена
