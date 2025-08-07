# Textarea

Textarea adds styling and autoResize functionality to standard textarea element.

## Import [#](https://primevue.org/textarea/#import)

```

import Textarea from 'primevue/textarea';


```

## Basic [#](https://primevue.org/textarea/#basic)

Textarea is used with the *v-model* property for two-way value binding.

```

<Textarea v-model="value" rows="5" cols="30" />


```

## Forms [#](https://primevue.org/textarea/#forms)

Textarea integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <Textarea name="address" rows="5" cols="30" style="resize: none" />
        <Message v-if="$form.address?.invalid" severity="error" size="small" variant="simple">{{ $form.address.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Auto Resize [#](https://primevue.org/textarea/#auto-resize)

When *autoResize* is enabled, textarea grows instead of displaying a scrollbar.

```

<Textarea v-model="value" autoResize rows="5" cols="30" />


```

## Filled [#](https://primevue.org/textarea/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

```

<Textarea v-model="value" variant="filled" rows="5" cols="30" />


```

## Float Label [#](https://primevue.org/textarea/#floatlabel)

A floating label appears on top of the input field when focused. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

Over LabelIn LabelOn Label

```

<FloatLabel>
    <Textarea id="over_label" v-model="value1" rows="5" cols="30" style="resize: none" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <Textarea id="over_label" v-model="value2" rows="5" cols="30" style="resize: none" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <Textarea id="over_label" v-model="value3" rows="5" cols="30" style="resize: none" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/textarea/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

Description

```

<IftaLabel>
    <Textarea id="description" v-model="value" rows="5" cols="30" style="resize: none" />
    <label for="description">Description</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/textarea/#sizes)

Textarea provides *small* and *large* sizes as alternatives to the base.

```

<Textarea v-model="value1" size="small" placeholder="Small" rows="3" />
<Textarea v-model="value2" placeholder="Normal" rows="3" />
<Textarea v-model="value3" size="large" placeholder="Large" rows="3" />


```

## Invalid [#](https://primevue.org/textarea/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

```

<Textarea v-model="value" rows="5" cols="30" :invalid="!value" style="resize: none" placeholder="Address" />


```

## Disabled [#](https://primevue.org/textarea/#disabled)

When *disabled* is present, the element cannot be edited and focused.

Disabled

```

<Textarea v-model="value" rows="5" cols="30" disabled />


```

## Accessibility [#](https://primevue.org/textarea/#accessibility)

### Screen Reader

Textarea component renders a native textarea element that implicitly includes any passed prop. Value to describe the component can either be provided via *label* tag combined with *id* prop or using *aria-labelledby*, *aria-label* props.

```

<label for="address1">Address 1</label>
<Textarea id="address1" />

<span id="address2">Address 2</span>
<Textarea aria-labelledby="address2" />

<Textarea aria-label="Address Details"/>


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the input. |