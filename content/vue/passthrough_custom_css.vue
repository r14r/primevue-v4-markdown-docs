import { createApp } from "vue";
import PrimeVue from "primevue/config";
const app = createApp(App);

app.use(PrimeVue, {
    pt: {
        global: {
            css: `
                .my-button {
                    border-width: 2px;
                }
            `
        },
        button: {
            root: 'my-button'
        }
    }
});