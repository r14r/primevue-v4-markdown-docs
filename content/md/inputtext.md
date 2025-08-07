# InputText

InputText is an extension to standard input element with theming.

## Import [#](https://primevue.org/inputtext/#import)

```

import InputText from 'primevue/inputtext';


```

## Basic [#](https://primevue.org/inputtext/#basic)

InputText is used with the *v-model* property for two-way value binding.

```

<InputText type="text" v-model="value" />


```

## Forms [#](https://primevue.org/inputtext/#forms)

InputText integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex justify-center flex-col gap-4">
    <div class="flex flex-col gap-1">
        <InputText name="username" type="text" placeholder="Username" />
        <Message v-if="$form.username?.invalid" severity="error" size="small" variant="simple">{{ $form.username.error?.message }}</Message>
    </div>
    <div class="flex flex-col gap-1">
        <InputText name="email" type="text" placeholder="Email" />
        <Message v-if="$form.email?.invalid" severity="error" size="small" variant="simple">{{ $form.email.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Filled [#](https://primevue.org/inputtext/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

```

<InputText type="text" v-model="value" variant="filled" />


```

## Float Label [#](https://primevue.org/inputtext/#floatlabel)

FloatLabel visually integrates a label with its form element. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

Over LabelIn LabelOn Label

```

<FloatLabel>
    <InputText id="over_label" v-model="value1" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <InputText id="in_label" v-model="value2" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <InputText id="on_label" v-model="value3" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/inputtext/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

Username

```

<IftaLabel>
    <InputText id="username" v-model="value" variant="filled" />
    <label for="username">Username</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/inputtext/#sizes)

InputText provides *small* and *large* sizes as alternatives to the base.

```

<InputText v-model="value1" type="text" size="small" placeholder="Small" />
<InputText v-model="value2" type="text" placeholder="Normal" />
<InputText v-model="value3" type="text" size="large" placeholder="Large" />


```

## Help Text [#](https://primevue.org/inputtext/#helptext)

An advisory text can be defined with the [Message](https://primevue.org/message) component.

Username

Enter your username to reset your password.

```

<div class="flex flex-col gap-2">
    <label for="username">Username</label>
    <InputText id="username" v-model="value" aria-describedby="username-help" />
    <Message size="small" severity="secondary" variant="simple">Enter your username to reset your password.</Message>
</div>


```

## Invalid [#](https://primevue.org/inputtext/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

```

<InputText v-model="value1" :invalid="!value1" placeholder="Name" />
<InputText v-model="value2" :invalid="!value2" variant="filled" placeholder="Name" />


```

## Disabled [#](https://primevue.org/inputtext/#disabled)

When *disabled* is present, the element cannot be edited and focused.

```

<InputText v-model="value" disabled placeholder="Disabled" />


```

## Accessibility [#](https://primevue.org/inputtext/#accessibility)

### Screen Reader

InputText component renders a native input element that implicitly includes any passed prop. Value to describe the component can either be provided via *label* tag combined with *id* prop or using *aria-labelledby*, *aria-label* props.

```

<label for="firstname">Firstname</label>
<InputText id="firstname" />

<span id="lastname">Lastname</span>
<InputText aria-labelledby="lastname" />

<InputText aria-label="Age"/>


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the input. |