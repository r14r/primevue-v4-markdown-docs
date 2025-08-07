# DatePicker

DatePicker is a form component for date inputs.

## Import [#](https://primevue.org/datepicker/#import)

```

import DatePicker from 'primevue/datepicker';


```

## Basic [#](https://primevue.org/datepicker/#basic)

DatePicker is used with the *v-model* property for two-way value binding.

```

<DatePicker v-model="date" />


```

## Forms [#](https://primevue.org/datepicker/#forms)

DatePicker integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <DatePicker name="date" fluid />
        <Message v-if="$form.date?.invalid" severity="error" size="small" variant="simple">{{ $form.date.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Format [#](https://primevue.org/datepicker/#format)

Default date format is *mm/dd/yy* which can be customized using the *dateFormat* property. Following options can be a part of the format.

* *d* - day of month (no leading zero)
* *dd* - day of month (two digit)
* *o* - day of the year (no leading zeros)
* *oo* - day of the year (three digit)
* *D* - day name short
* *DD* - day name long
* *m* - month of year (no leading zero)
* *mm* - month of year (two digit)
* *M* - month name short
* *MM* - month name long
* *y* - year (two digit)
* *yy* - year (four digit)
* *@* - Unix timestamp (ms since 01/01/1970)
* *!* - Windows ticks (100ns since 01/01/0001)
* *'...'* - literal text
* *''* - single quote
* *anything else* - literal text

```

<DatePicker v-model="date" dateFormat="dd/mm/yy" />


```

## Locale [#](https://primevue.org/datepicker/#locale)

Locale for different languages and formats is defined globally, refer to the [PrimeVue Locale](https://primevue.org/configuration/#locale) configuration for more information.

## Icon [#](https://primevue.org/datepicker/#icon)

An additional icon is displayed next to the input field when *showIcon* is present.

Button

Default Icon

Custom Icon

```

<DatePicker v-model="buttondisplay" showIcon fluid :showOnFocus="false" />
<DatePicker v-model="icondisplay" showIcon fluid iconDisplay="input" />
<DatePicker v-model="templatedisplay" showIcon fluid iconDisplay="input" timeOnly>
    <template #inputicon="slotProps">
        <i class="pi pi-clock" @click="slotProps.clickCallback" />
    </template>
</DatePicker>


```

## Min / Max [#](https://primevue.org/datepicker/#minmax)

Boundaries for the permitted dates that can be entered are defined with *minDate* and *maxDate* properties.

```

<DatePicker v-model="date" :minDate="minDate" :maxDate="maxDate" :manualInput="false" />


```

## Multiple [#](https://primevue.org/datepicker/#multiple)

In order to choose multiple dates, set *selectionMode* as *multiple*. In this mode, the value binding should be an array.

```

<DatePicker v-model="dates" selectionMode="multiple" :manualInput="false" />


```

## Range [#](https://primevue.org/datepicker/#range)

A range of dates can be selected by defining *selectionMode* as *range*, in this case the bound value would be an array with two values where first date is the start of the range and second date is the end.

```

<DatePicker v-model="dates" selectionMode="range" :manualInput="false" />


```

## Button Bar [#](https://primevue.org/datepicker/#button)

When *showButtonBar* is present, today and clear buttons are displayed at the footer.

```

<DatePicker v-model="date" showButtonBar />


```

## Time [#](https://primevue.org/datepicker/#time)

A time picker is displayed when *showTime* is enabled where 12/24 hour format is configured with *hourFormat* property. In case, only time needs to be selected, add *timeOnly* to hide the date section.

12h Format

24h Format

Time Only

```

<DatePicker id="datepicker-12h" v-model="datetime12h" showTime hourFormat="12" fluid />
<DatePicker id="datepicker-24h" v-model="datetime24h" showTime hourFormat="24" fluid />
<DatePicker id="datepicker-timeonly" v-model="time" timeOnly fluid />


```

## Month Picker [#](https://primevue.org/datepicker/#monthpicker)

Month only picker is enabled by specifying *view* as *month* in addition to a suitable *dateFormat*.

```

<DatePicker v-model="date" view="month" dateFormat="mm/yy" />


```

## Year Picker [#](https://primevue.org/datepicker/#yearpicker)

Specifying *view* as *year* in addition to a suitable *dateFormat* enables the year picker.

```

<DatePicker v-model="date" view="year" dateFormat="yy" />


```

## Multiple Months [#](https://primevue.org/datepicker/#multiplemonths)

Number of months to display is configured with the *numberOfMonths* property.

```

<DatePicker v-model="date" :numberOfMonths="2" />


```

## Date Template [#](https://primevue.org/datepicker/#datetemplate)

Custom content can be placed inside date cells with the *date* slot that takes a Date as a parameter.

```

<DatePicker v-model="date">
    <template #date="slotProps">
        <strong v-if="slotProps.date.day > 10 && slotProps.date.day < 15" style="text-decoration: line-through">{{ slotProps.date.day }}</strong>
        <template v-else>{{ slotProps.date.day }}</template>
    </template>
</DatePicker>


```

## Inline [#](https://primevue.org/datepicker/#inline)

DatePicker is displayed as a popup by default, add *inline* property to customize this behavior.

August2025

| Wk | Su | Mo | Tu | We | Th | Fr | Sa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 30 | 27 | 28 | 29 | 30 | 31 | 1 | 2 |
| 31 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 32 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| 33 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| 34 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
| 35 | 31 | 1 | 2 | 3 | 4 | 5 | 6 |

```

<DatePicker v-model="date" inline showWeek class="w-full sm:w-[30rem]" />


```

## Filled [#](https://primevue.org/datepicker/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

```

<DatePicker v-model="date" variant="filled" />


```

## Float Label [#](https://primevue.org/datepicker/#floatlabel)

A floating label appears on top of the input field when focused. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

Over LabelIn LabelOn Label

```

<FloatLabel>
    <DatePicker v-model="value1" inputId="over_label" showIcon iconDisplay="input" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <DatePicker v-model="value2" inputId="in_label" showIcon iconDisplay="input" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <DatePicker v-model="value3" inputId="on_label" showIcon iconDisplay="input" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/datepicker/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

Date

```

<IftaLabel>
    <DatePicker v-model="value" inputId="date" showIcon iconDisplay="input" variant="filled" />
    <label for="date">Date</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/datepicker/#sizes)

DatePicker provides *small* and *large* sizes as alternatives to the base.

```

<DatePicker v-model="value1" size="small" placeholder="Small" showIcon iconDisplay="input" />
<DatePicker v-model="value2" placeholder="Normal" showIcon iconDisplay="input" />
<DatePicker v-model="value3" size="large" placeholder="Large" showIcon iconDisplay="input" />


```

## Invalid [#](https://primevue.org/datepicker/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

```

<DatePicker v-model="date1" :invalid="!date1" placeholder="Date" />
<DatePicker v-model="date2" :invalid="!date2" variant="filled" placeholder="Date" />


```

## Disabled [#](https://primevue.org/datepicker/#disabled)

DatePicker is used a controlled input component with *v-model* property.

```

<DatePicker v-model="date" disabled />


```

## Accessibility [#](https://primevue.org/datepicker/#accessibility)

### Screen Reader

Value to describe the component can either be provided via *label* tag combined with *inputId* prop or using *aria-labelledby*, *aria-label* props. The input element has *combobox* role in addition to *aria-autocomplete* as "none", *aria-haspopup* as "dialog" and *aria-expanded* attributes. The relation between the input and the popup is created with *aria-controls* attribute that refers to the id of the popup.

The optional datepicker button requires includes *aria-haspopup*, *aria-expanded* for states along with *aria-controls* to define the relation between the popup and the button. The value to read is retrieved from the *chooseDate* key of the aria property from the [locale](https://primevue.org/configuration/#locale) API. This label is also used for the *aria-label* of the popup as well. When there is a value selected, it is formatted and appended to the label to be able to notify users about the current value.

Popup has a *dialog* role along with *aria-modal* and *aria-label*. The navigation buttons at the header has an *aria-label* retrieved from the *prevYear*, *nextYear*, *prevMonth*, *nextMonth*, *prevDecade* and *nextDecade* keys of the locale aria API. Similarly month picker button uses the *chooseMonth* and year picker button uses the *chooseYear* keys.

Main date table uses *grid* role that contains th elements with *col* as the scope along with *abbr* tag resolving to the full name of the month. Each date cell has an *aria-label* referring to the full date value. Buttons at the footer utilize their readable labels as *aria-label* as well. Selected date also receives the *aria-selected* attribute.

Timepicker spinner buttons get their labels for *aria-label* from the aria locale API using the *prevHour*, *nextHour*, *prevMinute*, *nextMinute*, *prevSecond*, *nextSecond*, *am* and *pm* keys.

DatePicker also includes a hidden section that is only available to screen readers with *aria-live* as "polite". This element is updated when the selected date changes to instruct the user about the current date selected.

```

<label for="date1">Date</label>
<DatePicker inputId="date1" />

<span id="date2">Date</span>
<DatePicker aria-labelledby="date2" />

<DatePicker aria-label="Date" />


```

### Choose Date Button Keyboard Support

| Key | Function |
| --- | --- |
| *space* | Opens popup and moves focus to the selected date, if there is none focuses on today. |
| *enter* | Opens popup and moves focus to the selected date, if there is none focuses on today. |

### Popup Keyboard Support

| Key | Function |
| --- | --- |
| *escape* | Closes the popup and moves focus to the input element. |
| *tab* | Moves focus to the next focusable element within the popup. |
| *shift* + *tab* | Moves focus to the next focusable element within the popup. |

### Header Buttons Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Triggers the button action. |
| *space* | Triggers the button action. |

### Date Grid Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Selects the date, closes the popup and moves focus to the input element. |
| *space* | Closes the popup and moves focus to the input element. |
| *up arrow* | Moves focus to the same day of the previous week. |
| *alt* + *up arrow* | Closes the popup and moves focus to the input element. |
| *down arrow* | Moves focus to the same day of the next week. |
| *right arrow* | Moves focus to the next day. |
| *left arrow* | Moves focus to the previous day. |
| *home* | Moves focus to the first day of the current week. |
| *end* | Moves focus to the last day of the current week. |
| *page up* | Changes the date to previous month in date picker mode. Moves to previous year in month picker mode and previous decade in year picker. |
| *shift* + *page up* | Changes the date to previous year in date picker mode. Has no effect in month or year picker. |
| *page down* | Changes the date to next month in date picker mode. Moves to next year in month picker mode and next decade in year picker. |
| *shift* + *page down* | Changes the date to next year in date picker mode. Has no effect in month or year picker. |

### Footer Buttons Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Triggers the button action. |
| *space* | Triggers the button action. |