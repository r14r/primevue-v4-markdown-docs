# Unstyled Mode

Theming PrimeVue with alternative styling approaches.

## Architecture [#](https://primevue.org/theming/unstyled/#architecture)

The term *unstyled* is used to define an alternative styling approach instead of the default theming with design tokens. In unstyled mode the css variables of the design tokens and the css rule sets that utilize them are not included. Here is an example of an Unstyled Select, the core functionality and accessibility is provided whereas styling is not included. Unstyled components still need to be styled on your end, in the next sections, we'll cover the styling solutions for both modes.

Unstyled Select

## Setup [#](https://primevue.org/theming/unstyled/#setup)

Unstyled mode is enabled for the whole suite by enabling *unstyled* option during PrimeVue installation.

```

import { createApp } from "vue";
import PrimeVue from "primevue/config";
const app = createApp(App);

app.use(PrimeVue, { unstyled: true });


```

Alternatively even in the default styled mode, a particular component can still be used as unstyled by adding the *unstyled* prop of the component.

Check

```

<Button label="Check" icon="pi pi-check" unstyled></Button>


```

## Example [#](https://primevue.org/theming/unstyled/#example)

Here is a sample that styles a button component with Tailwind CSS using [pass through](https://primevue.org/passthrough) attributes. Before beginning, head over to the the pass through section at [button](https://primevue.org/button) documentation to learn more about the components internals section. We'll be using the *root*, *label* and *icon* elements to add a custom style.

Search

```

<Button
    label="Search"
    icon="pi pi-search"
    unstyled
    pt:root="bg-teal-500 hover:bg-teal-700 active:bg-teal-900 cursor-pointer py-2 px-4 rounded-full border-0 flex gap-2"
    pt:label="text-white font-bold text-lg"
    pt:icon="text-white text-xl"
/>


```

## Global [#](https://primevue.org/theming/unstyled/#global)

A global configuration can be created at application level to avoid repetition via the global *pt* option so that the styles can be shared from a single location. A particular component can still override a global configuration with its own *pt* property.

```

import { createApp } from "vue";
import PrimeVue from "primevue/config";
const app = createApp(App);

app.use(PrimeVue, {
    unstyled: true,
    pt: {
        button: {
            root: 'bg-teal-500 hover:bg-teal-700 active:bg-teal-900 cursor-pointer py-2 px-4 rounded-full border-0 flex gap-2',
            label: 'text-white font-bold text-lg',
            icon: 'text-white text-xl'
        },
        panel: {
            header: 'bg-primary text-primary-contrast border-primary',
            content: 'border-primary text-lg text-primary-700',
            title: 'bg-primary text-primary-contrast text-xl',
            toggler: 'bg-primary text-primary-contrast hover:text-primary hover:bg-primary-contrast'
        }
    }
});


```

## Volt [#](https://primevue.org/theming/unstyled/#volt)

Tailwind CSS is perfect fit for the unstyled mode, PrimeTek has initiated a new UI library called [Volt](https://volt.primevue.org) based on the unstyled PrimeVue and Tailwind CSS v4. Volt follows the code ownership model where the components are located in the application codebase rather than node\_modules. All components within Volt are essentially wrapped versions of the unstyled PrimeVue equivalents, with an added layer of theming through Tailwind CSS v4. This approach, along with the templating features, offers complete control over the theming and presentation.