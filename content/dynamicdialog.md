# Dynamic Dialog

Dialogs can be created dynamically with any component as the content using a DialogService.

## Import [#](https://primevue.org/dynamicdialog/#import)

```

import DynamicDialog from 'primevue/dynamicdialog';


```

## Dialog Service [#](https://primevue.org/dynamicdialog/#dialogservice)

A single shared dialog instance is required in the application, ideal location would be defining it once at the main application template.

```

<DynamicDialog />


```

A dynamic dialog is controlled via the *DialogService* that needs to be installed as an application plugin.

```

import {createApp} from 'vue';
import DialogService from 'primevue/dialogservice';

const app = createApp(App);
app.use(DialogService);


```

The service is available with the *useDialog* function for Composition API or using the *$dialog* property of the application for Options API.

```

/* Composition API */
import { useDialog } from 'primevue/usedialog';

const dialog = useDialog();

/* Options API */
const dialog = this.$dialog;


```

## Open [#](https://primevue.org/dynamicdialog/#open)

The *open* function of the *DialogService* is used to open a Dialog. First parameter is the component to load and second one is the configuration object to customize the Dialog.

```

import ProductListDemo from './ProductListDemo';
import { useDialog } from 'primevue/usedialog';

const dialog = useDialog();

const showProducts = () => {
    dialog.open(ProductListDemo, {});
}


```

The component can also be loaded asynchronously, this approach is useful in conditional cases and to improve initial load times as well.

```

import { useDialog } from 'primevue/usedialog';

const dialog = useDialog();

const dynamicComponent = defineAsyncComponent(() => import('./ProductListDemo.vue'));

const showProducts = () => {
    dialog.open(dynamicComponent, {});
}


```

## Customization [#](https://primevue.org/dynamicdialog/#customization)

DynamicDialog uses the Dialog component internally, visit [dialog](https://primevue.org/dialog) for more information about the available props.

```

import ProductListDemo from './ProductListDemo';
import { useDialog } from 'primevue/usedialog';

const dialog = useDialog();

const showProducts = () => {
    dialog.open(ProductListDemo, {
        props: {
            header: 'Product List',
            style: {
                width: '50vw',
            },
            breakpoints:{
                '960px': '75vw',
                '640px': '90vw'
            },
            modal: true
        }
    });
}


```

## Close [#](https://primevue.org/dynamicdialog/#close)

The *close* function is available through a *dialogRef* that is injected to the component loaded by the dialog.

```

import { inject } from "vue";

const dialogRef = inject('dialogRef');

const closeDialog = () => {
    dialogRef.value.close();
}


```

## Passing Data [#](https://primevue.org/dynamicdialog/#passingdata)

Use the *data* property to pass parameters when opening a Dialog, the internal component can later access this data using *dialogRef*.

```

const dialog = useDialog();

const showProducts = () => {
    dialog.open(ProductListDemo, {
        data: {
            user: 'primetime'
        }
    });
}


```

```

import { inject, onMounted } from "vue";

const dialogRef = inject('dialogRef');

onMounted(() => {
    const params = dialogRef.value.data; // {user: 'primetime'}
})


```

Similarly when hiding a Dialog, any parameter passed to the *close* function is received from the *onClose* callback.

```

const dialog = useDialog();

const showProducts = () => {
    dialog.open(ProductListDemo, {
        onClose: (opt) => {
            const callbackParams = opt.data; // {selectedId: 12}
        }
    });
}


```

```

import { inject } from "vue";

const dialogRef = inject('dialogRef');

const closeDialog = () => {
    dialogRef.value.close({
        selectedId: 12
    });
}


```

## Events [#](https://primevue.org/dynamicdialog/#events)

The *emits* object defines callbacks to handle events emitted by the component within the Dialog.

```

import ProductListDemo from './ProductListDemo';
import { useDialog } from 'primevue/usedialog';

const dialog = useDialog();

const showProducts = () => {
    dialog.open(ProductListDemo, {
        emits: {
            onCancel: (e) => {
                console.log(e);  // {user: 'primetime'}
            },
            onSave: (e) => {
                console.log(e);  // {user: 'primetime'}
            }
        }
    });
}


```

```

<script setup>
/* ProductListDemo.vue */
const emit = defineEmits(['cancel', 'save'])

function buttonClick() {
    emit('cancel', {user: 'primetime'});
}

function saveButtonClick() {
    emit('save', {user: 'primetime'});
}
</script>


```

## Example [#](https://primevue.org/dynamicdialog/#example)

A sample implementation to demonstrate loading components asynchronously, nested content and passing data.

Select a Product

```

<Button label="Select a Product" icon="pi pi-search" @click="showProducts" />

<DynamicDialog />


```

## Accessibility [#](https://primevue.org/dynamicdialog/#accessibility)

Visit accessibility section of [dialog](https://primevue.org/dialog/#accessibility) component for more information.