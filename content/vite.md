# Install PrimeVue with Vite

Setting up PrimeVue in a Vite project.

## Download [#](https://primevue.org/vite/#download)

PrimeVue is available for download on [npm registry](https://www.npmjs.com/package/primevue).

```

# Using npm
npm install primevue @primeuix/themes

# Using yarn
yarn add primevue @primeuix/themes

# Using pnpm
pnpm add primevue @primeuix/themes


```

## Plugin [#](https://primevue.org/vite/#theme)

PrimeVue plugin is required to be installed as an application plugin to set up the default [configuration](https://primevue.org/configuration). The plugin is lightweight, and only utilized for configuration purposes.

```

import { createApp } from 'vue';
import PrimeVue from 'primevue/config';

const app = createApp(App);
app.use(PrimeVue);


```

## Theme [#](https://primevue.org/vite/#theme)

Configure PrimeVue to use a theme like Aura.

```

import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';

const app = createApp(App);
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});


```

## Verify [#](https://primevue.org/vite/#verify)

Verify your setup by adding a component such as [Button](https://primevue.org/button). Each component can be imported and registered individually so that you only include what you use for bundle optimization. Import path is available in the documentation of the corresponding component.

Verify

```

import Button from "primevue/button"

const app = createApp(App);
app.component('Button', Button);


```

## Examples [#](https://primevue.org/vite/#examples)

We've created various samples for the popular options in the Vue ecosystem. Visit the [primevue-examples](https://github.com/primefaces/primevue-examples) repository for more samples including [vite-quickstart](https://github.com/primefaces/primevue-examples/tree/main/vite-quickstart) and [vite-ts-quickstart](https://github.com/primefaces/primevue-examples/tree/main/vite-ts-quickstart).

## Video [#](https://primevue.org/vite/#video)

Watch the short video tutorial from Çağatay Çivici to setup PrimeVue in styled mode with [Create-Vue](https://github.com/vuejs/create-vue).

## Next Steps [#](https://primevue.org/vite/#nextsteps)

Welcome to the Prime UI Ecosystem! Once you have PrimeVue up and running, we recommend exploring the following resources to gain a deeper understanding of the library.

* [Global configuration](https://primevue.org/configuration)
* [Auto imports with tree-shaking](https://primevue.org/autoimport)
* [Customization of styles](https://primevue.org/theming/styled)
* [Pass through attributes](https://primevue.org/passthrough)
* [Getting support](https://primevue.org/support)