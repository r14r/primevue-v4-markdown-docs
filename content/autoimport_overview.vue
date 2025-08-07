import { createApp } from "vue";
import PrimeVue from "primevue/config";
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import App from './App.vue'
const app = createApp(App);

app.use(PrimeVue);
app.component('InputText', InputText);
app.component('Button', Button);