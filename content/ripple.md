# Ripple

Ripple directive adds ripple effect to the host element.

## Import [#](https://primevue.org/ripple/#import)

Ripple is an optional animation for the supported components such as buttons. It is disabled by default and needs to be enabled at your app's entry file (e.g. main.js) during the PrimeVue setup.

```

import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
const app = createApp(App);

app.use(PrimeVue, { ripple: true });


```

Ripple describes how to use it with your own components and standard elements that needs to be imported and configured with a name of your choice. Global configuration is done with the *app.directive* function.

```

import Ripple from 'primevue/ripple';

app.directive('ripple', Ripple);


```

## Configuration [#](https://primevue.org/ripple/#configuration)

To start with, Ripple needs to be enabled globally. See the [Configuration API](https://primevue.org/configuration/#ripple) for details.

```

mounted() {
    this.$primevue.config.ripple = true;
}


```

## Default [#](https://primevue.org/ripple/#default)

Ripple is enabled by adding add *p-ripple* class to the target and attach the directive with the v- prefix.

Ripple option at the  configurator needs to be turned on for the demo.

Default

```

<div v-ripple class="ripple-box">Default</div>


```

## Custom [#](https://primevue.org/ripple/#custom)

Default styling of the animation adds a shade of white. This can easily be customized using css that changes the color of *p-ink* element.

Ripple option at the  configurator needs to be turned on for the demo.

Green

Orange

Purple

```

<div v-ripple class="box" style="border: 1px solid rgba(75, 175, 80, 0.3); --p-ripple-background: rgba(75, 175, 80, 0.3)">Green</div>
<div v-ripple class="box" style="border: 1px solid rgba(255, 193, 6, 0.3); --p-ripple-background: rgba(255, 193, 6, 0.3)">Orange</div>
<div v-ripple class="box" style="border: 1px solid rgba(156, 39, 176, 0.3); --p-ripple-background: rgba(156, 39, 176, 0.3)">Purple</div>


```

## Accessibility [#](https://primevue.org/ripple/#accessibility)

### Screen Reader

Ripple element has the *aria-hidden* attribute as true so that it gets ignored by the screen readers.

### Keyboard Support

Component does not include any interactive elements.