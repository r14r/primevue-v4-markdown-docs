# Auto Import

On-demand PrimeVue components with auto imports and tree-shaking.

## Overview [#](https://primevue.org/autoimport/#overview)

PrimeVue components need to be imported and configured individually. In the next section, we'll cleanup the code using auto imports.

```

import { createApp } from "vue";
import PrimeVue from "primevue/config";
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import App from './App.vue'
const app = createApp(App);

app.use(PrimeVue);
app.component('InputText', InputText);
app.component('Button', Button);


```

## Unplugin [#](https://primevue.org/autoimport/#unplugin)

The [unplugin-vue-components](https://github.com/unplugin/unplugin-vue-components) library can automatically import and register PrimeVue components with the help of *@primevue/auto-import-resolver*. Begin with installing the packages as dev dependencies.

```

npm i unplugin-vue-components -D
npm i @primevue/auto-import-resolver -D


```

Next step would be adding the *PrimeVueResolver* at vite.config using the *Components* plugin.

```

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite';
import {PrimeVueResolver} from '@primevue/auto-import-resolver';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [
        PrimeVueResolver()
      ]
    })
  ]
})


```

That's it, now the initialization code can be refactored as the following. For configuration like namespacing, visit the [official documentation](https://github.com/unplugin/unplugin-vue-components?tab=readme-ov-file#configuration).

```

import { createApp } from "vue";
import PrimeVue from "primevue/config";
import App from './App.vue'
const app = createApp(App);

app.use(PrimeVue);


```

## Example [#](https://primevue.org/autoimport/#example)

A complete example using PrimeVue with auto imports is available at the [playground](https://primevue.org/playground).