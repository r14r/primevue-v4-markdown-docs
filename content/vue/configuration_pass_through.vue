import { createApp } from "vue";
import PrimeVue from "primevue/config";
const app = createApp(App);

app.use(PrimeVue, {
    pt: {
        slider: {
            handle: { class: 'bg-primary text-primary-contrast' }
        }
    }
});