# RadioButton

RadioButton is an extension to standard radio button element with theming.

## Import [#](https://primevue.org/radiobutton/#import)

```

import RadioButton from 'primevue/radiobutton';
import RadioButtonGroup from 'primevue/radiobuttongroup';


```

## Group [#](https://primevue.org/radiobutton/#group)

RadioButton is used with the *v-model* property for two-way value binding.

Cheese

Mushroom

Pepper

Onion

```

<div class="flex flex-wrap gap-4">
    <div class="flex items-center gap-2">
        <RadioButton v-model="ingredient" inputId="ingredient1" name="pizza" value="Cheese" />
        <label for="ingredient1">Cheese</label>
    </div>
    <div class="flex items-center gap-2">
        <RadioButton v-model="ingredient" inputId="ingredient2" name="pizza" value="Mushroom" />
        <label for="ingredient2">Mushroom</label>
    </div>
    <div class="flex items-center gap-2">
        <RadioButton v-model="ingredient" inputId="ingredient3" name="pizza" value="Pepper" />
        <label for="ingredient3">Pepper</label>
    </div>
    <div class="flex items-center gap-2">
        <RadioButton v-model="ingredient" inputId="ingredient4" name="pizza" value="Onion" />
        <label for="ingredient4">Onion</label>
    </div>
</div>


```

## Forms [#](https://primevue.org/radiobutton/#forms)

RadioButton integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Cheese

Mushroom

Pepper

Onion

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-2">
        <RadioButtonGroup name="ingredient" class="flex flex-wrap gap-4">
            <div class="flex items-center gap-2">
                <RadioButton inputId="cheese" value="Cheese" />
                <label for="cheese">Cheese</label>
            </div>
            <div class="flex items-center gap-2">
                <RadioButton inputId="mushroom" value="Mushroom" />
                <label for="mushroom">Mushroom</label>
            </div>
            <div class="flex items-center gap-2">
                <RadioButton inputId="pepper" value="Pepper" />
                <label for="pepper">Pepper</label>
            </div>
            <div class="flex items-center gap-2">
                <RadioButton inputId="onion" value="Onion" />
                <label for="onion">Onion</label>
            </div>
        </RadioButtonGroup>
        <Message v-if="$form.ingredient?.invalid" severity="error" size="small" variant="simple">{{ $form.ingredient.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Dynamic [#](https://primevue.org/radiobutton/#dynamic)

RadioButtons can be generated using a list of values.

Accounting

Marketing

Production

Research

```

<div v-for="category in categories" :key="category.key" class="flex items-center gap-2">
    <RadioButton v-model="selectedCategory" :inputId="category.key" name="dynamic" :value="category.name" />
    <label :for="category.key">{{ category.name }}</label>
</div>


```

## Filled [#](https://primevue.org/radiobutton/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

```

<RadioButton v-model="value" value="1" variant="filled" />


```

## Sizes [#](https://primevue.org/radiobutton/#sizes)

RadioButton provides *small* and *large* sizes as alternatives to the base.

Small

Normal

Large

```

<div class="flex flex-wrap gap-4">
    <div class="flex items-center gap-2">
        <RadioButton v-model="size" inputId="size_small" name="size" value="Small" size="small" />
        <label for="size_small" class="text-sm">Small</label>
    </div>
    <div class="flex items-center gap-2">
        <RadioButton v-model="size" inputId="size_normal" name="size" value="Normal" />
        <label for="size_normal">Normal</label>
    </div>
    <div class="flex items-center gap-2">
        <RadioButton v-model="size" inputId="size_large" name="size" value="Large" size="large" />
        <label for="size_large" class="text-lg">Large</label>
    </div>
</div>


```

## Invalid [#](https://primevue.org/radiobutton/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

```

<RadioButton v-model="value" value="1" :invalid="value === null" />


```

## Disabled [#](https://primevue.org/radiobutton/#disabled)

When *disabled* is present, the element cannot be edited and focused.

```

<RadioButton v-model="value" :value="1" disabled />
<RadioButton v-model="value" :value="2" disabled />


```

## Accessibility [#](https://primevue.org/radiobutton/#accessibility)

### Screen Reader

RadioButton component uses a hidden native radio button element internally that is only visible to screen readers. Value to describe the component can either be provided via *label* tag combined with *id* prop or using *aria-labelledby*, *aria-label* props.

```

<label for="rb1">One</label>
<RadioButton inputId="rb1" />

<span id="rb2">Two</span>
<RadioButton aria-labelledby="rb2" />

<RadioButton aria-label="Three" />


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the checked radio button, if there is none within the group then first radio button receives the focus. |
| *left arrow**up arrow* | Moves focus to the previous radio button, if there is none then last radio button receives the focus. |
| *right arrow**down arrow* | Moves focus to the next radio button, if there is none then first radio button receives the focus. |
| *space* | If the focused radio button is unchecked, changes the state to checked. |