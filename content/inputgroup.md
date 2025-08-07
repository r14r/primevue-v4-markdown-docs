# InputGroup

Text, icon, buttons and other content can be grouped next to an input.

## Import [#](https://primevue.org/inputgroup/#import)

```

import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';


```

## Basic [#](https://primevue.org/inputgroup/#basic)

A group is created by wrapping the input and add-ons with the *InputGroup* component. Each add-on element is defined as a child of *InputGroupAddon* component.

$

.00

www

City

```

<InputGroup>
    <InputGroupAddon>
        <i class="pi pi-user"></i>
    </InputGroupAddon>
    <InputText v-model="text1" placeholder="Username" />
</InputGroup>

<InputGroup>
    <InputGroupAddon>$</InputGroupAddon>
    <InputNumber v-model="number" placeholder="Price" />
    <InputGroupAddon>.00</InputGroupAddon>
</InputGroup>

<InputGroup>
    <InputGroupAddon>www</InputGroupAddon>
    <InputText v-model="text2" placeholder="Website" />
</InputGroup>

<InputGroup>
    <InputGroupAddon>
        <i class="pi pi-map"></i>
    </InputGroupAddon>
    <Select v-model="selectedCity" :options="cities" optionLabel="name" placeholder="City" />
</InputGroup>


```

## Multiple [#](https://primevue.org/inputgroup/#multiple)

Multiple add-ons can be placed inside the same group.

$

.00

```

<InputGroup class="sm:!w-96">
    <InputGroupAddon>
        <i class="pi pi-clock"></i>
    </InputGroupAddon>
    <InputGroupAddon>
        <i class="pi pi-star-fill"></i>
    </InputGroupAddon>
    <InputNumber placeholder="Price" />
    <InputGroupAddon>$</InputGroupAddon>
    <InputGroupAddon>.00</InputGroupAddon>
</InputGroup>


```

## Button [#](https://primevue.org/inputgroup/#button)

Buttons can be placed at either side of an input element.

Search

```

<InputGroup>
    <Button label="Search" />
    <InputText placeholder="Keyword" />
</InputGroup>

<InputGroup>
    <InputText placeholder="Keyword" />
    <InputGroupAddon>
        <Button icon="pi pi-search" severity="secondary" variant="text" @click="toggle" />
    </InputGroupAddon>
</InputGroup>
<Menu ref="menu" :model="items" popup class="!min-w-fit" />

<InputGroup>
    <InputGroupAddon>
        <Button icon="pi pi-check" severity="secondary" />
    </InputGroupAddon>
    <InputText placeholder="Vote" />
    <InputGroupAddon>
        <Button icon="pi pi-times" severity="secondary" />
    </InputGroupAddon>
</InputGroup>


```

## Checkbox & Radio [#](https://primevue.org/inputgroup/#checkbox)

Checkbox and RadioButton components can be combined with an input element under the same group.

```

<InputGroup>
    <InputText placeholder="Price" />
    <InputGroupAddon>
        <RadioButton v-model="radioValue1" name="rb1" value="rb1" />
    </InputGroupAddon>
</InputGroup>

<InputGroup>
    <InputGroupAddon>
        <Checkbox v-model="checked1" :binary="true" />
    </InputGroupAddon>
    <InputText placeholder="Username" />
</InputGroup>

<InputGroup>
    <InputGroupAddon>
        <Checkbox v-model="checked2" :binary="true" />
    </InputGroupAddon>
    <InputText placeholder="Website" />
    <InputGroupAddon>
        <RadioButton v-model="radioValue2" name="rb2" value="rb2" />
    </InputGroupAddon>
</InputGroup>


```

## Float Label [#](https://primevue.org/inputgroup/#floatlabel)

FloatLabel visually integrates a label with its form element. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

Over Label

$

In Label

.00

www

On Label

```

<InputGroup>
    <InputGroupAddon>
        <i class="pi pi-user"></i>
    </InputGroupAddon>
    <FloatLabel>
        <InputText id="over_label" v-model="value1" />
        <label for="over_label">Over Label</label>
    </FloatLabel>
</InputGroup>

<InputGroup>
    <InputGroupAddon>$</InputGroupAddon>
    <FloatLabel variant="in">
        <InputText id="in_label" v-model="value2" />
        <label for="in_label">In Label</label>
    </FloatLabel>
    <InputGroupAddon>.00</InputGroupAddon>
</InputGroup>

<InputGroup>
    <InputGroupAddon>www</InputGroupAddon>
    <FloatLabel variant="on">
        <InputText id="on_label" v-model="value3" />
        <label for="on_label">On Label</label>
    </FloatLabel>
</InputGroup>


```

## Ifta Label [#](https://primevue.org/inputgroup/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

Price

```

<InputGroup class="md:w-80">
    <InputGroupAddon>
        <i class="pi pi-shopping-cart"></i>
    </InputGroupAddon>
    <IftaLabel>
        <InputNumber v-model="value" inputId="price" mode="currency" currency="USD" locale="en-US" />
        <label for="price">Price</label>
    </IftaLabel>
</InputGroup>


```

## Accessibility [#](https://primevue.org/inputgroup/#accessibility)

### Screen Reader

InputGroup and InputGroupAddon do not require any roles and attributes.

### Keyboard Support

Component does not include any interactive elements.