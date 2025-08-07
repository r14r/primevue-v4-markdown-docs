import { createApp } from "vue";
import PrimeVue from "primevue/config";
const app = createApp(App);

app.use(PrimeVue, {
    pt: {
        panel: {
            header: {
                class: 'bg-primary text-primary-contrast'
            }
        },
        autocomplete: {
            input: {
                root: 'w-64' // OR { class: 'w-64' }
            }
        }
    }
});