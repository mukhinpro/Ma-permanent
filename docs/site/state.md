# Сайт — SEO и состояние

## Сделано

- ✅ SEO-чеклист Wix закрыт **106/106** (10 сентября: последними были alt text на Home и meta description у Privacy Policy)
- ✅ H1/H2 на всех страницах услуг + добавлено «in Los Angeles»
- ✅ Виджеты Wix Bookings «Избранная услуга» с ценами на страницах услуг
- ✅ FAQ-аккордеоны через элемент «Сворачивающийся текст» Wix Classic Editor — **72 вопроса на 9 услуг**, EN + RU-перевод
- ✅ Privacy Policy на `/privacy-policy` (скрыта из навигации, ссылка в футере)
- ✅ robots.txt открыт для AI-краулеров (GPTBot, ClaudeBot, PerplexityBot); PetalBot заблокирован
- ✅ NLWeb + llms.txt + MCP endpoint живые
- ✅ GEO-чеклист для 6 районных страниц (Beverly Hills, Century City, Brentwood, Santa Monica, Culver City, Bel Air)
- ⚠️ Доступность: репитерные заголовки намеренно оставлены H2. Реальные проблемы: нет H1 на Book Lash Extensions, H6 перед H1 на Home, пропуски уровней на Contact

## Правки 13 сентября — Nano & Combo Brows (опубликовано)

Решение и контекст — см. `docs/google-ads/state.md`, раздел про закрытие рассогласования Combo Brows.

**Wix Bookings:**
- Услуга «Nano Eyebrows» → **«Nano & Combo Brows»**, id `c9304d62-918f-4175-844e-6432f252883f` (revision 19 на момент правки). Подтверждено повторным query
- Цена не менялась: в Bookings уже стоит $550 с зачёркнутой $480 (Summer Special)

**Страница `/nanobrows` (Wix Classic Editor):**
- H1 `#section1part1title1`: «Nano Brows» → «Nano & Combo Brows». Заголовок 6, DIN Neuzeit Grotesk 26px; подстрока «in Los Angeles» выставлена 16px
- В существующий текстовый блок `#section1part1p1`, после абзаца «The result: thicker, natural…», добавлен **один новый абзац**:
  > We also offer Combo Brows — a combination of the hair-stroke technique and soft powder shading. Hair strokes define the front of the brow and the direction of natural growth, while gentle powder shading adds fullness and shape to the rest of the brow for a soft, beautifully finished look.
- Существующий текст про Nano Brows **не удалялся и не переписывался**. Секция «Nano Brows vs. Microblading», цены и FAQ не тронуты
- Новый графический блок не заводился — сознательное решение, чтобы не ломать вёрстку

**Сайт сохранён и опубликован.** Проверено на живой странице: изменения на месте, виджет бронирования показывает «Nano & Combo Brows / 2 hr 30 min / $550 → $480».

⚠️ **Инцидент при работе через Wix API:** query по `name $startsWith "Nano"` вернул два результата, и первой была переименована не та услуга — «Nano / Powder Brows Touch-Up» (id `bfb170cb-712d-4fac-b240-4d96beb42a98`). Ошибка замечена и откачена сразу, имя восстановлено. **Правило:** перед update по имени всегда проверять, сколько записей вернул query.

## 🔴 Открытые задачи

1. **Опубликовать сайт целиком** — FAQ-аккордеоны, Schema.org, фикс Instagram сидят в черновике
2. **Проверить дубли страниц:** `/services-1`, `/book-eyelash-extensions2`, `/копия-копия-book-eyelash-extensions`
3. После публикации — Google Rich Results Test
4. **Bing Webmaster Tools** — регистрация не сделана, только вручную через браузер, API нет. ChatGPT Search сильно опирается на индекс Bing → приоритет
5. Скорость: сейчас ~2.1s, цель <2s — сжать картинки, проверить сторонние виджеты
6. Проверить через view-source на 6 районных постах, что `article:author` и BlogPosting JSON-LD с «Александр Мухин» больше не рендерятся (теги обновлены 2 сентября, JSON-LD заменён на Organization, BLOG_POST паттерн сброшен в дефолт)
7. Полный аудит по 10 факторам ранжирования
8. Проверить schema.org на всех страницах
9. Privacy Policy: нет email для privacy-запросов, мобильная вёрстка не проверена

## Gift certificate flow (Wix / Velo)

- Поля получателя/отправителя `#input1`, `#input2` на странице корзины
- Данные пишутся в `buyerNote` через `backend/giftNote.web.js`
- `backend/events.js` парсит и сохраняет в CMS-коллекцию `GiftCertificates`
- ⚠️ Кнопка Checkout в Side Cart не решена — Side Cart вешает редактор/расширение, Alex переключит вручную
