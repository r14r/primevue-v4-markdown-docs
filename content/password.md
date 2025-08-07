# Password

Password displays strength indicator for password fields.

## Import [#](https://primevue.org/password/#import)

```

import Password from 'primevue/password';


```

## Basic [#](https://primevue.org/password/#basic)

Password is used with the *v-model* property for two-way value binding.

```

<Password v-model="value" :feedback="false" />


```

## Forms [#](https://primevue.org/password/#forms)

InputText is used with the *v-model* property.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full sm:w-64">
    <div class="flex flex-col gap-1">
        <Password name="password" placeholder="Password" :feedback="false" fluid />
        <template v-if="$form.password?.invalid">
            <Message v-for="(error, index) of $form.password.errors" :key="index" severity="error" size="small" variant="simple">{{ error.message }}</Message>
        </template>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Meter [#](https://primevue.org/password/#meter)

Strength meter is displayed as a popup while a value is being entered.

```

<Password v-model="value" />


```

## Locale [#](https://primevue.org/password/#locale)

Labels are translated at component level by *promptLabel*, *weakLabel*, *mediumLabel* and *strongLabel* properties. In order to apply global translations for all Password components in the application, refer to the [locale](https://primevue.org/configuration/#locale).

```

<Password v-model="value" promptLabel="Choose a password" weakLabel="Too simple" mediumLabel="Average complexity" strongLabel="Complex password" />


```

## ToggleMask [#](https://primevue.org/password/#togglemask)

When *toggleMask* is present, an icon is displayed to show the value as plain text.

```

<Password v-model="value" toggleMask />


```

## Template [#](https://primevue.org/password/#template)

3 slots are included to customize the overlay. These are *header*, *content* and *footer*. Note that content overrides the default meter.

```

<Password v-model="value">
    <template #header>
        <div class="font-semibold text-xm mb-4">Reset Password</div>
    </template>
    <template #footer>
        <Divider />
        <ul class="pl-2 my-0 leading-normal text-sm">
            <li>At least one lowercase</li>
            <li>At least one uppercase</li>
            <li>At least one numeric</li>
            <li>Minimum 8 characters</li>
        </ul>
    </template>
</Password>


```

## Filled [#](https://primevue.org/password/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

```

<Password v-model="value" :feedback="false" variant="filled" />


```

## Float Label [#](https://primevue.org/password/#floatlabel)

A floating label appears on top of the input field when focused. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

Over LabelIn LabelOn Label

```

<FloatLabel>
    <Password v-model="value1" inputId="over_label" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <Password v-model="value2" inputId="in_label" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <Password v-model="value3" inputId="on_label" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/password/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

Password

```

<IftaLabel>
    <Password v-model="value" inputId="password" variant="filled" />
    <label for="password">Password</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/password/#sizes)

Password provides *small* and *large* sizes as alternatives to the base.

```

<div class="card flex flex-col items-center gap-4">
    <Password v-model="value1" size="small" placeholder="Small" />
    <Password v-model="value2" placeholder="Normal" />
    <Password v-model="value3" size="large" placeholder="Large" />
</div>


```

## Invalid [#](https://primevue.org/password/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

```

<Password v-model="value1" :invalid="!value1" placeholder="Password" />
<Password v-model="value2" :invalid="!value2" variant="filled" placeholder="Password" />


```

## Disabled [#](https://primevue.org/password/#disabled)

When *disabled* is present, the element cannot be edited and focused.

```

<Password disabled placeholder="Disabled" />


```

## Accessibility [#](https://primevue.org/password/#accessibility)

### Screen Reader

Value to describe the component can either be provided via *label* tag combined with *id* prop or using *aria-labelledby*, *aria-label* props. Screen reader is notified about the changes to the strength of the password using a section that has *aria-live* while typing.

```

<label for="pwd1">Password</label>
<Password inputId="pwd1" />

<span id="pwd2">Password</span>
<Password aria-labelledby="pwd2" />

<Password aria-label="Password"/>


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the input. |
| *escape* | Hides the strength meter if open. |