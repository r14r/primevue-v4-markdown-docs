import { useDialog } from 'primevue/usedialog';

const dialog = useDialog();

const dynamicComponent = defineAsyncComponent(() => import('./ProductListDemo.vue'));

const showProducts = () => {
    dialog.open(dynamicComponent, {});
}