# ConfirmDialog

ConfirmDialog uses a Dialog UI that is integrated with the Confirmation API.

## Import [#](https://primevue.org/confirmdialog/#import)

```

import ConfirmDialog from 'primevue/confirmdialog';


```

## Service [#](https://primevue.org/confirmdialog/#confirmation-service)

ConfirmDialog is controlled via the *ConfirmationService* that needs to be installed as an application plugin.

```

import {createApp} from 'vue';
import ConfirmationService from 'primevue/confirmationservice';

const app = createApp(App);
app.use(ConfirmationService);


```

The service is available with the *useConfirm* function for Composition API or using the *$confirm* property of the application for Options API.

```

import { useConfirm } from "primevue/useconfirm";

const confirm = useConfirm();


```

## Basic [#](https://primevue.org/confirmdialog/#basic)

ConfirmDialog is displayed by calling the *require* method of the *$confirm* instance by passing the options to customize the Dialog. The *target* attribute is mandatory to align the popup to its referrer.

SaveDelete

```

<ConfirmDialog></ConfirmDialog>
<Button @click="confirm1()" label="Save" variant="outlined"></Button>
<Button @click="confirm2()" label="Delete" severity="danger" variant="outlined"></Button>


```

## Position [#](https://primevue.org/confirmdialog/#position)

The *position* property of the confirm options specifies the location of the Dialog.

LeftRight

TopLeftTopTopRight

BottomLeftBottomBottomRight

```

<ConfirmDialog group="positioned"></ConfirmDialog>
<div class="flex flex-wrap justify-center gap-2 mb-4">
    <Button @click="confirmPosition('left')" icon="pi pi-arrow-right" label="Left" severity="secondary" style="min-width: 10rem"></Button>
    <Button @click="confirmPosition('right')" icon="pi pi-arrow-left" label="Right" severity="secondary" style="min-width: 10rem"></Button>
</div>
<div class="flex flex-wrap justify-center gap-2 mb-4">
    <Button @click="confirmPosition('topleft')" icon="pi pi-arrow-down-right" label="TopLeft" severity="secondary" style="min-width: 10rem"></Button>
    <Button @click="confirmPosition('top')" icon="pi pi-arrow-down" label="Top" severity="secondary" style="min-width: 10rem"></Button>
    <Button @click="confirmPosition('topright')" icon="pi pi-arrow-down-left" label="TopRight" severity="secondary" style="min-width: 10rem"></Button>
</div>
<div class="flex flex-wrap justify-center gap-2">
    <Button @click="confirmPosition('bottomleft')" icon="pi pi-arrow-up-right" label="BottomLeft" severity="secondary" style="min-width: 10rem"></Button>
    <Button @click="confirmPosition('bottom')" icon="pi pi-arrow-up" label="Bottom" severity="secondary" style="min-width: 10rem"></Button>
    <Button @click="confirmPosition('bottomright')" icon="pi pi-arrow-up-left" label="BottomRight" severity="secondary" style="min-width: 10rem"></Button>
</div>


```

## Template [#](https://primevue.org/confirmdialog/#template)

Templating allows customizing the message content.

Save

```

<ConfirmDialog group="templating">
    <template #message="slotProps">
        <div class="flex flex-col items-center w-full gap-4 border-b border-surface-200 dark:border-surface-700">
            <i :class="slotProps.message.icon" class="!text-6xl text-primary-500"></i>
            <p>{{ slotProps.message.message }}</p>
        </div>
    </template>
</ConfirmDialog>
<Button @click="showTemplate()" label="Save"></Button>


```

## Headless [#](https://primevue.org/confirmdialog/#headless)

Headless mode is enabled by defining a *container* slot that lets you implement entire confirmation UI instead of the default elements.

Save

```

<ConfirmDialog group="headless">
    <template #container="{ message, acceptCallback, rejectCallback }">
        <div class="flex flex-col items-center p-8 bg-surface-0 dark:bg-surface-900 rounded">
            <div class="rounded-full bg-primary text-primary-contrast inline-flex justify-center items-center h-24 w-24 -mt-20">
                <i class="pi pi-question !text-4xl"></i>
            </div>
            <span class="font-bold text-2xl block mb-2 mt-6">{{ message.header }}</span>
            <p class="mb-0">{{ message.message }}</p>
            <div class="flex items-center gap-2 mt-6">
                <Button label="Save" @click="acceptCallback" class="w-32"></Button>
                <Button label="Cancel" variant="outlined" @click="rejectCallback" class="w-32"></Button>
            </div>
        </div>
    </template>
</ConfirmDialog>
<Button @click="requireConfirmation()" label="Save"></Button>


```

## Accessibility [#](https://primevue.org/confirmdialog/#accessibility)

### Screen Reader

ConfirmDialog component uses *alertdialog* role along with *aria-labelledby* referring to the header element however any attribute is passed to the root element so you may use *aria-labelledby* to override this default behavior. In addition *aria-modal* is added since focus is kept within the popup.

When *require* method of the *$confirm* instance is used and a trigger is passed as a parameter, ConfirmDialog adds *aria-expanded* state attribute and *aria-controls* to the trigger so that the relation between the trigger and the dialog is defined.

```

<ConfirmDialog id="confirm" />

<Button @click="openDialog()" label="Confirm" :aria-expanded="visible" :aria-controls="visible ? 'confirm' : null"></Button>


```

```

<script setup>
const confirm = useConfirm();
const isVisible = ref(false);

const openDialog = () => {
    confirm.require({
        message: 'Are you sure you want to proceed?',
        header: 'Confirmation',
        onShow: () => {
            isVisible.value = true;
        },
        onHide: () => {
            isVisible.value = false;
        }
    });
};
</script>


```

### Overlay Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next the focusable element within the dialog. |
| *shift* + *tab* | Moves focus to the previous the focusable element within the dialog. |
| *escape* | Closes the dialog. |

### Buttons Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Closes the dialog. |
| *space* | Closes the dialog. |