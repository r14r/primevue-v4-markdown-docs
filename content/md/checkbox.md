# Checkbox

Checkbox is an extension to standard checkbox element with theming.

## Import [#](https://primevue.org/checkbox/#import)

```

import Checkbox from 'primevue/checkbox';
import CheckboxGroup from 'primevue/checkboxgroup';


```

## Basic [#](https://primevue.org/checkbox/#basic)

Binary checkbox is used with the *v-model* for two-way value binding and the *binary* property.

```

<Checkbox v-model="checked" binary />


```

## Group [#](https://primevue.org/checkbox/#group)

Multiple checkboxes can be grouped together.

Cheese

Mushroom

Pepper

Onion

```

<div class="card flex flex-wrap justify-center gap-4">
    <div class="flex items-center gap-2">
        <Checkbox v-model="pizza" inputId="ingredient1" name="pizza" value="Cheese" />
        <label for="ingredient1"> Cheese </label>
    </div>
    <div class="flex items-center gap-2">
        <Checkbox v-model="pizza" inputId="ingredient2" name="pizza" value="Mushroom" />
        <label for="ingredient2"> Mushroom </label>
    </div>
    <div class="flex items-center gap-2">
        <Checkbox v-model="pizza" inputId="ingredient3" name="pizza" value="Pepper" />
        <label for="ingredient3"> Pepper </label>
    </div>
    <div class="flex items-center gap-2">
        <Checkbox v-model="pizza" inputId="ingredient4" name="pizza" value="Onion" />
        <label for="ingredient4"> Onion </label>
    </div>
</div>


```

## Forms [#](https://primevue.org/checkbox/#forms)

Checkbox integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Cheese

Mushroom

Pepper

Onion

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex justify-center flex-col gap-4">
    <div class="flex flex-col gap-2">
        <CheckboxGroup name="ingredient" class="flex flex-wrap gap-4">
            <div class="flex items-center gap-2">
                <Checkbox inputId="cheese" value="Cheese" />
                <label for="cheese"> Cheese </label>
            </div>
            <div class="flex items-center gap-2">
                <Checkbox inputId="mushroom" value="Mushroom" />
                <label for="mushroom"> Mushroom </label>
            </div>
            <div class="flex items-center gap-2">
                <Checkbox inputId="pepper" value="Pepper" />
                <label for="pepper"> Pepper </label>
            </div>
            <div class="flex items-center gap-2">
                <Checkbox inputId="onion" value="Onion" />
                <label for="onion"> Onion </label>
            </div>
        </CheckboxGroup>
        <Message v-if="$form.ingredient?.invalid" severity="error" size="small" variant="simple">{{ $form.ingredient.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Dynamic [#](https://primevue.org/checkbox/#dynamic)

Checkboxes can be generated using a list of values.

Accounting

Marketing

Production

Research

```

<div v-for="category of categories" :key="category.key" class="flex items-center gap-2">
    <Checkbox v-model="selectedCategories" :inputId="category.key" name="category" :value="category.name" />
    <label :for="category.key">{{ category.name }}</label>
</div>


```

## Indeterminate [#](https://primevue.org/checkbox/#indeterminate)

When *indeterminate* is present, the checkbox masks the actual value visually.

```

<Checkbox v-model="checked" indeterminate binary />


```

## Filled [#](https://primevue.org/checkbox/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

```

<Checkbox v-model="checked" binary variant="filled" />


```

## Sizes [#](https://primevue.org/checkbox/#sizes)

Checkbox provides *small* and *large* sizes as alternatives to the base.

Small

Normal

Large

```

<div class="card flex flex-wrap justify-center gap-4">
    <div class="flex items-center gap-2">
        <Checkbox v-model="size" inputId="size_small" name="size" value="Small" size="small" />
        <label for="size_small" class="text-sm">Small</label>
    </div>
    <div class="flex items-center gap-2">
        <Checkbox v-model="size" inputId="size_normal" name="size" value="Normal" />
        <label for="size_normal">Normal</label>
    </div>
    <div class="flex items-center gap-2">
        <Checkbox v-model="size" inputId="size_large" name="size" value="Large" size="large" />
        <label for="size_large" class="text-lg">Large</label>
    </div>
</div>


```

## Invalid [#](https://primevue.org/checkbox/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

```

<Checkbox v-model="checked" :invalid="!checked"  binary />


```

## Disabled [#](https://primevue.org/checkbox/#disabled)

When *disabled* is present, the element cannot be edited and focused.

```

<Checkbox v-model="checked1" binary disabled />
<Checkbox v-model="checked2" binary disabled />


```

## Accessibility [#](https://primevue.org/checkbox/#accessibility)

### Screen Reader

Checkbox component uses a hidden native checkbox element internally that is only visible to screen readers. Value to describe the component can either be provided via *label* tag combined with *inputId* prop or using *aria-labelledby*, *aria-label* props.

```

<label for="chkbox1">Remember Me</label>
<Checkbox inputId="chkbox1" />

<span id="chkbox2">Remember Me</span>
<Checkbox aria-labelledby="chkbox2" />

<Checkbox aria-label="Remember Me" />


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the checkbox. |
| *space* | Toggles the checked state. |