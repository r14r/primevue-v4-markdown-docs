# Install PrimeVue with Laravel

Setting up PrimeVue in a Laravel project.

## Download [#](https://primevue.org/laravel/#download)

PrimeVue is available for download on [npm registry](https://www.npmjs.com/package/primevue).

```

# Using npm
npm install primevue @primeuix/themes

# Using yarn
yarn add primevue @primeuix/themes

# Using pnpm
pnpm add primevue @primeuix/themes


```

## Plugin [#](https://primevue.org/laravel/#theme)

PrimeVue plugin is required to be installed as an application plugin to set up the default [configuration](https://primevue.org/configuration). The plugin is lightweight, and only utilized for configuration purposes.

```

import { createApp } from 'vue';
import PrimeVue from 'primevue/config';

const app = createApp(App);
app.use(PrimeVue);


```

## Theme [#](https://primevue.org/laravel/#theme)

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

## Verify [#](https://primevue.org/laravel/#verify)

Verify your setup by adding a component such as [Button](https://primevue.org/button). Each component can be imported and registered individually so that you only include what you use for bundle optimization. Import path is available in the documentation of the corresponding component.

Verify

```

import Button from "primevue/button"

const app = createApp(App);
app.component('Button', Button);


```

## Examples [#](https://primevue.org/laravel/#examples)

We've created various samples for the popular options in the Vue ecosystem. Visit the [primevue-examples](https://github.com/primefaces/primevue-examples) repository for more samples including [laravel-quickstart](https://github.com/primefaces/primevue-examples/tree/main/laravel-quickstart) and [inertia-quickstart](https://github.com/primefaces/primevue-examples/tree/main/inertia-quickstart).

## Next Steps [#](https://primevue.org/laravel/#nextsteps)

Welcome to the Prime UI Ecosystem! Once you have PrimeVue up and running, we recommend exploring the following resources to gain a deeper understanding of the library.

* [Global configuration](https://primevue.org/configuration)
* [Auto imports with tree-shaking](https://primevue.org/autoimport)
* [Customization of styles](https://primevue.org/theming/styled)
* [Pass through attributes](https://primevue.org/passthrough)
* [Getting support](https://primevue.org/support)