# Install PrimeVue with CND

Setting up PrimeVue in a project using CDN.

## Script [#](https://primevue.org/cdn/#script)

You can use PrimeVue and Vue.js from a CDN with a script tag. This approach does not involve any build step, and is suitable for enhancing static HTML. This guide uses [unpkg](https://www.unpkg.com/) however other providers such as [jsdeliver](https://www.jsdelivr.com) and [cdnjs](https://cdnjs.com) can also be used.

```

https://unpkg.com/vue@3/dist/vue.global.js
https://unpkg.com/primevue/umd/primevue.min.js
https://unpkg.com/@primeuix/themes/umd/aura.js  // see theming for alternatives


```

## CreateApp [#](https://primevue.org/cdn/#createapp)

Create an app container element and setup the application using *createApp*.

```

<body>
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

    <div id="app">
    </div>

    <script>
        const { createApp, ref } = Vue;

        const app = createApp({
            setup() {

            }
        });

        app.mount('#app');
    </script>
</body>


```

## Plugin [#](https://primevue.org/cdn/#plugin)

PrimeVue plugin is required to be installed as an application plugin to set up the default [configuration](https://primevue.org/configuration).

```

app.use(PrimeVue.Config);


```

## Theming [#](https://primevue.org/cdn/#theming)

Include the theme preset via a script element after adding PrimeVue, valid options are Aura, Lara, Nora and Material.

```

<!-- <script src="https://unpkg.com/@primeuix/themes/umd/{preset}.js"></script> -->

<script src="https://unpkg.com/@primeuix/themes/umd/aura.js"></script>
<script src="https://unpkg.com/@primeuix/themes/umd/lara.js"></script>
<script src="https://unpkg.com/@primeuix/themes/umd/nora.js"></script>
<script src="https://unpkg.com/@primeuix/themes/umd/material.js"></script>


```

## Example [#](https://primevue.org/cdn/#example)

A complete example using a PrimeVue DatePicker. You can also view this sample live at [Stackblitz](https://stackblitz.com/edit/web-platform-jt1jz4?file=index.html).

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PrimeVue + CDN</title>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width" />
    </head>
    <body>
        <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
        <script src="https://unpkg.com/primevue/umd/primevue.min.js"></script>
        <script src="https://unpkg.com/@primeuix/themes/umd/aura.js"></script>

        <div id="app">
            <p-datepicker v-model="date"></p-datepicker>
            <br /><br />
            {{ date }}
        </div>

        <script>
            const { createApp, ref } = Vue;

            const app = createApp({
                setup() {
                const date = ref();

                return {
                    date
                };
                },
            });

            app.use(PrimeVue.Config, {
                theme: {
                    preset: PrimeUIX.Themes.Aura
                }
            });

            app.component('p-datepicker', PrimeVue.DatePicker);

            app.mount('#app');
        </script>
    </body>
</html>


```