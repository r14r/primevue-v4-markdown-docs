# ConfirmPopup

ConfirmPopup displays a confirmation overlay displayed relatively to its target.

## Import [#](https://primevue.org/confirmpopup/#import)

```

import ConfirmPopup from 'primevue/confirmpopup';


```

## Service [#](https://primevue.org/confirmpopup/#confirmation-service)

ConfirmPopup is controlled via the *ConfirmationService* that needs to be installed as an application plugin.

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

## Basic [#](https://primevue.org/confirmpopup/#basic)

ConfirmPopup is displayed by calling the *require* method of the *$confirm* instance by passing the options to customize the Popup. The *target* attribute is mandatory to align the popup to its referrer.

SaveDelete

```

<ConfirmPopup></ConfirmPopup>
<Button @click="confirm1($event)" label="Save" variant="outlined"></Button>
<Button @click="confirm2($event)" label="Delete" severity="danger" variant="outlined"></Button>


```

## Template [#](https://primevue.org/confirmpopup/#template)

Templating allows customizing the message content.

Save

```

<ConfirmPopup group="templating">
    <template #message="slotProps">
        <div class="flex flex-col items-center w-full gap-4 border-b border-surface-200 dark:border-surface-700 p-4 mb-4 pb-0">
            <i :class="slotProps.message.icon" class="!text-6xl text-primary-500"></i>
            <p>{{ slotProps.message.message }}</p>
        </div>
    </template>
</ConfirmPopup>
<Button @click="showTemplate($event)" label="Save"></Button>


```

## Headless [#](https://primevue.org/confirmpopup/#headless)

Headless mode is enabled by defining a *container* slot that lets you implement entire confirmation UI instead of the default elements.

Save

```

<ConfirmPopup group="headless">
    <template #container="{ message, acceptCallback, rejectCallback }">
        <div class="rounded p-4">
            <span>{{ message.message }}</span>
            <div class="flex items-center gap-2 mt-4">
                <Button label="Save" @click="acceptCallback" size="small"></Button>
                <Button label="Cancel" variant="outlined" @click="rejectCallback" severity="secondary" size="small" text></Button>
            </div>
        </div>
    </template>
</ConfirmPopup>
<Button @click="requireConfirmation($event)" label="Save"></Button>


```

## Accessibility [#](https://primevue.org/confirmpopup/#accessibility)

### Screen Reader

ConfirmPopup component uses *alertdialog* role and since any attribute is passed to the root element you may define attributes like *aria-label* or *aria-labelledby* to describe the popup contents. In addition *aria-modal* is added since focus is kept within the popup.

When *require* method of the *$confirm* instance is used and a trigger is passed as a parameter, ConfirmPopup adds *aria-expanded* state attribute and *aria-controls* to the trigger so that the relation between the trigger and the dialog is defined.

```

<ConfirmPopup id="confirm" aria-label="popup" />

<Button @click="openPopup($event)" label="Confirm" id="confirmButton" :aria-expanded="isVisible" :aria-controls="isVisible ? 'confirm' : null" />


```

```

<script setup>
const confirm = useConfirm();
const isVisible = ref(false);
const openPopup = (event) => {
    confirm.require({
        target: event.currentTarget,
        message: 'Are you sure you want to proceed?',
        header: 'Confirmation',
        onShow: () => {
            isVisible.value = true;
        },
        onHide: () => {
            isVisible.value = false;
        }
    });
}
</script>


```

### Overlay Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next the focusable element within the popup. |
| *shift* + *tab* | Moves focus to the previous the focusable element within the popup. |
| *escape* | Closes the popup and moves focus to the trigger. |

### Buttons Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Triggers the action, closes the popup and moves focus to the trigger. |
| *space* | Triggers the action, closes the popup and moves focus to the trigger. |