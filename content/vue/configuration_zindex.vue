import {createApp} from "vue";
import PrimeVue from "primevue/config";
const app = createApp(App);

app.use(PrimeVue, {
    zIndex: {
        modal: 1100,        //dialog, drawer
        overlay: 1000,      //select, popover
        menu: 1000,         //overlay menus
        tooltip: 1100       //tooltip
    }
});