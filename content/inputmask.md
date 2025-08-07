# InputMask

InputMask component is used to enter input in a certain format such as numeric, date, currency, email and phone.

## Import [#](https://primevue.org/inputmask/#import)

```

import InputMask from 'primevue/inputmask';


```

## Basic [#](https://primevue.org/inputmask/#basic)

InputMask is used with the *v-model* property for two-way value binding.

```

<InputMask id="basic" v-model="value" mask="99-999999" placeholder="99-999999" />


```

## Forms [#](https://primevue.org/inputmask/#forms)

InputMask integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full sm:w-56">
    <div class="flex flex-col gap-1">
        <InputMask name="serialNumber" mask="99-999999" placeholder="99-999999" fluid />
        <Message v-if="$form.serialNumber?.invalid" severity="error" size="small" variant="simple">{{ $form.serialNumber.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Mask [#](https://primevue.org/inputmask/#mask)

Mask format can be a combination of the following definitions; *a* for alphabetic characters, *9* for numeric characters and *\** for alphanumberic characters. In addition, formatting characters like *(*, *)* , *-* are also accepted.

SSN

Phone

Serial

```

<div class="flex-auto">
    <label for="ssn" class="font-bold block mb-2">SSN</label>
    <InputMask id="ssn" v-model="value1" mask="999-99-9999" placeholder="999-99-9999" fluid />
</div>

<div class="flex-auto">
    <label for="phone" class="font-bold block mb-2">Phone</label>
    <InputMask id="phone" v-model="value2" mask="(999) 999-9999" placeholder="(999) 999-9999" fluid />
</div>

<div class="flex-auto">
    <label for="serial" class="font-bold block mb-2">Serial</label>
    <InputMask id="serial" v-model="value3" mask="a*-999-a999" placeholder="a*-999-a999" fluid />
</div>


```

## Optional [#](https://primevue.org/inputmask/#optional)

When the input does not complete the mask definition, it is cleared by default. Use *autoClear* property to control this behavior. In addition, *?* is used to mark anything after the question mark optional.

```

<InputMask v-model="value" mask="(999) 999-9999? x99999" placeholder="(999) 999-9999? x99999" />


```

## SlotChar [#](https://primevue.org/inputmask/#slotchar)

Default placeholder for a mask is underscore that can be customized using *slotChar* property.

```

<InputMask id="basic" v-model="value" placeholder="99/99/9999" mask="99/99/9999" slotChar="mm/dd/yyyy" />


```

## Filled [#](https://primevue.org/inputmask/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

```

<InputMask id="basic" v-model="value" variant="filled" mask="99-999999" placeholder="99-999999" />


```

## Float Label [#](https://primevue.org/inputmask/#floatlabel)

FloatLabel visually integrates a label with its form element. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

Over LabelIn LabelOn Label

```

<FloatLabel>
    <InputMask id="over_label" v-model="value1" mask="999-99-9999" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <InputMask id="in_label" v-model="value2" mask="999-99-9999" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <InputMask id="on_label" v-model="value3" mask="999-99-9999" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/inputmask/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

SSN

```

<IftaLabel>
    <InputMask id="ssn" v-model="value" mask="999-99-9999" variant="filled" />
    <label for="ssn">SSN</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/inputmask/#sizes)

InputMask provides *small* and *large* sizes as alternatives to the base.

```

<InputMask v-model="value1" placeholder="Small" size="small" mask="99-999999" />
<InputMask v-model="value2" placeholder="Normal" mask="99-999999" />
<InputMask v-model="value3" placeholder="Large" size="large" mask="99-999999" />


```

## Invalid [#](https://primevue.org/inputmask/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

```

<InputMask v-model="value1" mask="99-999999" placeholder="Serial Key" :invalid="!value1" />
<InputMask v-model="value2" mask="99-999999" placeholder="Serial Key" :invalid="!value2" variant="filled" />


```

## Disabled [#](https://primevue.org/inputmask/#disabled)

When *disabled* is present, the element cannot be edited and focused.

```

<InputMask mask="99-999999" placeholder="Disabled" disabled />


```

## Accessibility [#](https://primevue.org/inputmask/#accessibility)

### Screen Reader

InputMask component renders a native input element that implicitly includes any passed prop. Value to describe the component can either be provided via *label* tag combined with *id* prop or using *aria-labelledby*, *aria-label* props.

```

<label for="date">Date</label>
<InputMask id="date" />

<span id="phone">Phone</span>
<InputMask aria-labelledby="phone" />

<InputMask aria-label="Age" />


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the input. |