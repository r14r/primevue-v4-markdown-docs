# Fluid

Fluid is a layout component to make descendant components span full width of their container.

## Import [#](https://primevue.org/fluid/#import)

```

import Fluid from 'primevue/fluid';


```

## Basic [#](https://primevue.org/fluid/#basic)

Components with the *fluid* option like *InputText* have the ability to span the full width of their component. Enabling the *fluid* for each component individually may be cumbersome so wrap the content with *Fluid* to instead for an easier alternative.

Any component that has the *fluid* property can be nested inside the *Fluid* component. The *fluid* property of a child component has higher precedence than the fluid container as shown in the last sample.

Non-Fluid

Fluid Prop

Fluid Container

```

<div>
    <label for="non-fluid" class="font-bold mb-2 block">Non-Fluid</label>
    <InputText id="non-fluid" />
</div>

<div>
    <label for="fluid" class="font-bold mb-2 block">Fluid Prop</label>
    <InputText id="fluid" fluid />
</div>

<Fluid>
    <span class="font-bold mb-2 block">Fluid Container</span>
    <div class="grid grid-cols-2 gap-4">
        <div><InputText /></div>
        <div><InputText /></div>
        <div class="col-span-full"><InputText /></div>
        <div><InputText :fluid="false" placeholder="Non-Fluid" /></div>
    </div>
</Fluid>


```

## Accessibility [#](https://primevue.org/fluid/#accessibility)

### Screen Reader

Fluid does not require any roles and attributes.

### Keyboard Support

Component does not include any interactive elements.