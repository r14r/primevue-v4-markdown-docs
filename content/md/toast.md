# Toast

Toast is used to display messages in an overlay.

## Import [#](https://primevue.org/toast/#import)

```

import Toast from 'primevue/toast';


```

## Toast Service [#](https://primevue.org/toast/#toast-service)

Toast component is controlled via the *ToastService* that needs to be installed as an application plugin.

```

import {createApp} from 'vue';
import ToastService from 'primevue/toastservice';

const app = createApp(App);
app.use(ToastService);


```

The service is available with the *useToast* function for Composition API or using the *$toast* property of the application for Options API.

```

import { useToast } from 'primevue/usetoast';

const toast = useToast();


```

## Basic [#](https://primevue.org/toast/#basic)

Ideal location of a Toast is the main application template so that it can be used by any component within the application. A single message is represented by the Message interface that defines properties such as severity, summary and detail.

Show

```

<Toast />
<Button label="Show" @click="show()" />


```

## Severity [#](https://primevue.org/toast/#severity)

The *severity* option specifies the type of the message.

SuccessInfoWarnErrorSecondaryContrast

```

<Toast />
<Button label="Success" severity="success" @click="showSuccess" />
<Button label="Info" severity="info" @click="showInfo" />
<Button label="Warn" severity="warn" @click="showWarn" />
<Button label="Error" severity="danger" @click="showError" />
<Button label="Secondary" severity="secondary" @click="showSecondary" />
<Button label="Contrast" severity="contrast" @click="showContrast" />


```

## Position [#](https://primevue.org/toast/#position)

A message can be targeted to a certain Toast component by matching the *group* keys whereas location is customized with the *position*.

Top LeftBottom LeftBottom Right

```

<Toast position="top-left" group="tl" />
<Toast position="bottom-left" group="bl" />
<Toast position="bottom-right" group="br" />

<Button label="Top Left" @click="showTopLeft" />
<Button label="Bottom Left" @click="showBottomLeft" />
<Button label="Bottom Right" @click="showBottomRight" />


```

## Multiple [#](https://primevue.org/toast/#multiple)

Multiple messages are displayed by passing an array to the *show* method.

Multiple

```

<Toast />
<Button label="Multiple" @click="showMultiple()" />


```

## Sticky [#](https://primevue.org/toast/#sticky)

A message disappears after the number of milliseconds defined in the *life* option. Omit the *life* option to make the message sticky.

StickyClear

```

<Toast />
<Button @click="showSticky" label="Sticky" />
<Button label="Clear" severity="secondary" @click="clear()" />


```

## Template [#](https://primevue.org/toast/#template)

Custom content inside a message is defined with the *message* template.

View

```

<Toast position="bottom-center" group="bc" @close="onClose">
    <template #message="slotProps">
        <div class="flex flex-col items-start flex-auto">
            <div class="flex items-center gap-2">
                <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
                <span class="font-bold">Amy Elsner</span>
            </div>
            <div class="font-medium text-lg my-4">{{ slotProps.message.summary }}</div>
            <Button size="small" label="Reply" severity="success" @click="onReply()"></Button>
        </div>
    </template>
</Toast>
<Button @click="showTemplate" label="View" />


```

## Headless [#](https://primevue.org/toast/#headless)

Headless mode is enabled by defining a *container* slot that lets you implement entire toast UI instead of the default elements.

View

```

<Toast position="top-center" group="headless" @close="visible = false">
    <template #container="{ message, closeCallback }">
        <section class="flex flex-col p-4 gap-4 w-full bg-primary/70 rounded-xl">
            <div class="flex items-center gap-5">
                <i class="pi pi-cloud-upload text-white dark:text-black text-2xl"></i>
                <span class="font-bold text-base text-white dark:text-black">{{ message.summary }}</span>
            </div>
            <div class="flex flex-col gap-2">
                <ProgressBar :value="progress" :showValue="false" :style="{ height: '4px' }" pt:value:class="!bg-primary-50 dark:!bg-primary-900" class="!bg-primary/80"></ProgressBar>
                <label class="text-sm font-bold text-white dark:text-black">{{ progress }}% uploaded</label>
            </div>
            <div class="flex gap-4 mb-4 justify-end">
                <Button label="Another Upload?" size="small" @click="closeCallback"></Button>
                <Button label="Cancel" size="small" @click="closeCallback"></Button>
            </div>
        </section>
    </template>
</Toast>
<Button @click="show" label="View" />


```

## Accessibility [#](https://primevue.org/toast/#accessibility)

### Screen Reader

Toast component use *alert* role that implicitly defines *aria-live* as "assertive" and *aria-atomic* as "true".

Close element is a *button* with an *aria-label* that refers to the *aria.close* property of the [locale](https://primevue.org/configuration/#locale) API by default, you may use *closeButtonProps* to customize the element and override the default *aria-label*.

### Close Button Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Closes the message. |
| *space* | Closes the message. |