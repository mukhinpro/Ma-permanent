# Wix API — что работает, а что нет

## ✅ Работает

```
GET  https://www.wixapis.com/promote-seo-robots-server/v2/robots        # robots.txt чтение/запись
GET  https://www.wixapis.com/locale-settings/v2/settings
POST https://www.wixapis.com/_api/bookings-reader/v2/extended-bookings/query   # withEcomOrder: true
POST https://www.wixapis.com/ecom/v1/orders/search
     → priceSummary.total.amount, balanceSummary.paid.amount, balanceSummary.balance.amount
```

eCommerce orders read — работает.

## ❌ Не работает (Classic Editor)

- Per-page SEO (title, meta, noindex, H1)
- URL redirects — только дашборд
- Structured data / schema
- Page publish status
- **Alt text через Update File Descriptor** → `UNSUPPORTED_FIELD_MASK_PATH`.
  Обновляемы только `parentFolderId`, `displayName`, `labels`, `internalTags`.
  Alt text — вручную: редактор → картинка → Настройки → SEO/Alt text, либо Dashboard → SEO и GEO → Чек-лист → страница → «Добавить alt-текст».

## Поиск по документации

Использовать `Wix:SearchWixAPISpec` с JS-фильтром по `lightIndex` (name + docsUrl + menuPath) — надёжнее, чем `SearchWixRESTDocumentation`.

## Wix Editor — автоматизация через claude-in-chrome

- **Side Cart стабильно вешает расширение** — не автоматизировать вообще
- Репитеры делят один HTML-тег; карточки внутри репитера не могут иметь разные уровни заголовков
- Смена семантического тега: текст → «Редактировать» → «SEO и спецвозможности» → «Выберите тег HTML»
- Селектор страниц: **(264, 60)**
- Публикация: клик ~**(1438–1492, 20)**, ждать 20–30 с
- Monaco editor: найти модель по URI, `ed.executeEdits()` на полном range
- Аккордеоны SEO-чеклиста схлопываются при любом клике/фокусе внутри → заполнять через `javascript_tool` (native value setter + input event, потом клик «Применить и опубликовать» в том же скрипте)
- Мобильное приложение Wix не имеет кнопки «Опубликовать» и ненадёжно синкает блокировки календаря — управлять через десктоп
