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
