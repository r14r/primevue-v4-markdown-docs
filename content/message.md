# Message

Message component is used to display inline messages.

## Import [#](https://primevue.org/message/#import)

```

import Message from 'primevue/message';


```

## Basic [#](https://primevue.org/message/#basic)

Message component requires a content to display.

Message Content

```

<Message>Message Content</Message>


```

## Severity [#](https://primevue.org/message/#severity)

The *severity* option specifies the type of the message.

Success Message

Info Message

Warn Message

Error Message

Secondary Message

Contrast Message

```

<Message severity="success">Success Message</Message>
<Message severity="info">Info Message</Message>
<Message severity="warn">Warn Message</Message>
<Message severity="error">Error Message</Message>
<Message severity="secondary">Secondary Message</Message>
<Message severity="contrast">Contrast Message</Message>


```

## Icon [#](https://primevue.org/message/#icon)

Icon property and the *icon* slots are available to customize the icon of the message.

Info Message

How may I help you?

```

<Message severity="info" icon="pi pi-send">Info Message</Message>
<Message severity="success">
    <template #icon>
        <Avatar image="/images/avatar/amyelsner.png" shape="circle" />
    </template>
    <span class="ml-2">How may I help you?</span>
</Message>


```

## Outlined [#](https://primevue.org/message/#outlined)

Configure the *variant* value as *outlined* for messages with borders and no background.

Success Message

Info Message

Warn Message

Error Message

Secondary Message

Contrast Message

```

<Message severity="success" variant="outlined">Success Message</Message>
<Message severity="info" variant="outlined">Info Message</Message>
<Message severity="warn" variant="outlined">Warn Message</Message>
<Message severity="error" variant="outlined">Error Message</Message>
<Message severity="secondary" variant="outlined">Secondary Message</Message>
<Message severity="contrast" variant="outlined">Contrast Message</Message>


```

## Simple [#](https://primevue.org/message/#simple)

Configure the *variant* value as *simple* for messages without borders, backgrounds and paddings.

Success Message

Info Message

Warn Message

Error Message

Secondary Message

Contrast Message

```

<Message severity="success" variant="simple">Success Message</Message>
<Message severity="info" variant="simple">Info Message</Message>
<Message severity="warn" variant="simple">Warn Message</Message>
<Message severity="error" variant="simple">Error Message</Message>
<Message severity="secondary" variant="simple">Secondary Message</Message>
<Message severity="contrast" variant="simple">Contrast Message</Message>


```

## Sizes [#](https://primevue.org/message/#sizes)

Message provides *small* and *large* sizes as alternatives to the base.

Small Message

Normal Message

Large Message

```

<Message size="small" icon="pi pi-send">Small Message</Message>
<Message icon="pi pi-user">Normal Message</Message>
<Message size="large" icon="pi pi-check">Large Message</Message>


```

## Forms [#](https://primevue.org/message/#forms)

Validation errors in a form are displayed with the *error* severity.

Validation error

Username is required

Email is not valid

```

<Message v-if="!username || !email" severity="error" icon="pi pi-times-circle" class="mb-2">Validation error</Message>
<Message v-if="username && email" severity="success" icon="pi pi-times-circle" class="mb-2">Form is valid</Message>
<div class="flex flex-col gap-1">
    <InputText v-model="username" placeholder="Username" aria-label="username" :invalid="!username" />
    <Message v-if="!username" severity="error" variant="simple" size="small">Username is required</Message>
</div>
<div class="flex flex-col gap-1">
    <InputText v-model="email" placeholder="Email" aria-label="email" :invalid="!email" />
    <Message v-if="!email" severity="error" variant="simple" size="small">Email is not valid</Message>
</div>


```

## Dynamic [#](https://primevue.org/message/#dynamic)

Multiple messages can be displayed using the standard v-for directive.

ShowClear

```

<Button label="Show" @click="addMessages()" />
<Button label="Clear" severity="secondary" class="ml-2" @click="clearMessages()" />
<transition-group name="p-message" tag="div" class="flex flex-col">
    <Message v-for="msg of messages" :key="msg.id" :severity="msg.severity" class="mt-4">{{ msg.content }}</Message>
</transition-group>


```

## Closable [#](https://primevue.org/message/#closable)

Enable *closable* option to display an icon to remove a message.

Closable Message

```

<Message closable>Closable Message</Message>


```

## Life [#](https://primevue.org/message/#life)

Messages can disappear automatically by defined the *life* in milliseconds.

Show

```

<Button label="Show" @click="showMessage" :disabled="visible" class="mb-4" />
<Message v-if="visible" severity="success" :life="3000">Auto Disappear Message</Message>


```

## Accessibility [#](https://primevue.org/message/#accessibility)

### Screen Reader

Message component uses *alert* role that implicitly defines *aria-live* as "assertive" and *aria-atomic* as "true". Since any attribute is passed to the root element, attributes like *aria-labelledby* and *aria-label* can optionally be used as well.

Close element is a *button* with an *aria-label* that refers to the *aria.close* property of the [locale](https://primevue.org/configuration/#locale) API by default, you may use *closeButtonProps* to customize the element and override the default *aria-label*.

### Close Button Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Closes the message. |
| *space* | Closes the message. |