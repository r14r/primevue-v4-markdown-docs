# Install PrimeVue with Nuxt

Setting up PrimeVue in a Nuxt project.

## Download [#](https://primevue.org/nuxt/#download)

PrimeVue is available for download on [npm registry](https://www.npmjs.com/package/primevue) along with the official [@primevue/nuxt-module](https://www.npmjs.com/package/@primevue/nuxt-module).

```

# Using npm
npm install primevue @primeuix/themes
npm install --save-dev @primevue/nuxt-module

# Using yarn
yarn add primevue @primeuix/themes
yarn add --dev @primevue/nuxt-module

# Using pnpm
pnpm add primevue @primeuix/themes
pnpm add -D @primevue/nuxt-module


```

## Module [#](https://primevue.org/nuxt/#module)

In *nuxt.config* file, add the *@primevue/nuxt-module* to the modules section and define *primevue* object for the configuration of the module.

```

export default defineNuxtConfig({
    modules: [
        '@primevue/nuxt-module'
    ],
    primevue: {
        /* Configuration */
    }
})


```

## Theme [#](https://primevue.org/nuxt/#theme)

Configure the module to use a theme like Aura.

```

import Aura from '@primeuix/themes/aura';

export default defineNuxtConfig({
    modules: [
        '@primevue/nuxt-module'
    ],
    primevue: {
        options: {
            theme: {
                preset: Aura
            }
        }
    }
})


```

## Verify [#](https://primevue.org/nuxt/#verify)

The nuxt-primevue module registers the components automatically with tree-shaking support so you may start using them instantly.

Verify

```

<Button label="Verify" />


```

## Configuration [#](https://primevue.org/nuxt/#configuration)

### usePrimeVue [#](https://primevue.org/nuxt/#useprimevue)

The module installs the PrimeVue plugin by default. Disable this option if you prefer to configure PrimeVue manually e.g. with a Nuxt plugin.

```

primevue: {
    usePrimeVue: true | false
}


```

### options [#](https://primevue.org/nuxt/#options)

Main configuration settings of PrimeVue, refer to the [configuration](https://primevue.org/configuration/) documentation for details.

```

import Aura from '@primeuix/themes/aura';

export default defineNuxtConfig({
    modules: [
        '@primevue/nuxt-module'
    ],
    primevue: {
        options: {
            ripple: true,
            inputVariant: 'filled',
            theme: {
                preset: Aura,
                options: {
                    prefix: 'p',
                    darkModeSelector: 'system',
                    cssLayer: false
                }
            }
        }
    }
})


```

### autoImport [#](https://primevue.org/nuxt/#autoimport)

The [auto import](https://primevue.org/autoimport) feature registers components automatically with tree shaking support. Defaults to *true*, when disabled use include/exclude options of *components* and *directives* for manual registration.

```

primevue: {
    autoImport: true|false
}


```

Use the *prefix* in *components* and *directives* to add a prefix for registration.

```

primevue: {
    autoImport: true|false,
    components: {
        prefix: 'org'
    },
    directives: {
        prefix: 'org'
    }
}


```

### importPT [#](https://primevue.org/nuxt/#importpt)

Configures the global pass through import path.

```

primevue: {
    importPT: { from: '@/passthrough/mycustompt.js' }
}


```

*mycustompt.js* file defines the configuration and exports it.

```

const MyCustomPT = {
    ...
    button: {
        root: 'my-button',
       ...
    },
    ...
}

export default MyCustomPT;


```

### importTheme [#](https://primevue.org/nuxt/#importtheme)

Configures the theme configuration path for the customizations of a theme in styled mode.

```

primevue: {
    importTheme: { from: '@/themes/mytheme.js' },
}


```

The *mytheme.js* file contains the theme configuration.

```

import { definePreset } from '@primeuix/themes';
import Aura from '@primeuix/themes/aura';

const MyPreset = definePreset(Aura, {
    semantic: {
        primary: {
            50: '{indigo.50}',
            100: '{indigo.100}',
            200: '{indigo.200}',
            300: '{indigo.300}',
            400: '{indigo.400}',
            500: '{indigo.500}',
            600: '{indigo.600}',
            700: '{indigo.700}',
            800: '{indigo.800}',
            900: '{indigo.900}',
            950: '{indigo.950}'
        }
    }
});

export default {
    preset: MyPreset,
    options: {
        darkModeSelector: '.p-dark'
    }
};



```

### components [#](https://primevue.org/nuxt/#components)

When *autoImport* is disabled, use the *include* and *exclude* for manual registration.

The components to import and register are defined with the *include* option using a string array. When the value is ignored or set using the *\** alias, all of the components are registered.

```

primevue: {
    components: {
        include: ['Button', 'DataTable']
    }
}


```

In case all components are imported, particular components can still be excluded with the *exclude* option.

```

primevue: {
    components: {
        include: '*',
        exclude: ['Galleria', 'Carousel']
    }
}


```

By default, for compatibility reasons, Chart and Editor components are excluded. To include them simply set the *exclude* option to an empty list.

```

primevue: {
    components: {
        exclude: []
    }
}


```

Use the *prefix* option to give a prefix to the registered component names.

```

primevue: {
    components: {
        prefix: 'Prime'
        include: ['Button', 'DataTable']    /* Used as <PrimeButton /> and <PrimeDataTable /> */
    }
}


```

Component registration can be customized further by implementing the *name* function that gets an object representing the import metadata. *name* is the label of the component, *as* is the default export name and *from* is the import path.

```

primevue: {
    components: {
        name: ({ name, as, from }) => {
            return name === 'Button' ? `My${name}` : name;
        },
        include: ['Button', 'DataTable']    /* Used as <MyButton /> and <DataTable /> */
    }
}


```

### directives [#](https://primevue.org/nuxt/#directives)

When *autoImport* is disabled, use the *include* and *exclude* for manual registration.

The names of the directives to import and register are provided using the *include* property. When the value is ignored or set using the *\** alias, all of the directives are registered.

```

primevue: {
    directives: {
        include: ['Ripple', 'Tooltip']
    }
}


```

Similar to components, certain directives can be excluded and name registration can be customized.

```

primevue: {
    directives: {
        include: '*',
        exclude: ['Ripple']
    }
}


```

```

primevue: {
    directives: {
        prefix: 'p'
        include: ['Ripple', 'Tooltip']    /* Used as v-pripple and v-ptooltip */
    }
}


```

### composables [#](https://primevue.org/nuxt/#composables)

Determines the composables to use, when default value is ignored or set as *\** all composables are imported.

```

primevue: {
    composables: {
        include: ['useStyle']
    }
}


```

## Examples [#](https://primevue.org/nuxt/#examples)

[Nuxt based samples](https://github.com/primefaces/primevue-examples/tree/main/nuxt-quickstart) with different options are available at PrimeVue examples repository.

## Next Steps [#](https://primevue.org/nuxt/#nextsteps)

Welcome to the Prime UI Ecosystem! Once you have PrimeVue up and running, we recommend exploring the following resources to gain a deeper understanding of the library.

* [Global configuration](https://primevue.org/configuration)
* [Customization of styles](https://primevue.org/theming/styled)
* [Pass through attributes](https://primevue.org/passthrough)
* [Getting support](https://primevue.org/support)