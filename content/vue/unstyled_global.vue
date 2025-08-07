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