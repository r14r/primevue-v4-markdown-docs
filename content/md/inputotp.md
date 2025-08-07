# InputOtp

Input Otp is used to enter one time passwords.

## Import [#](https://primevue.org/inputotp/#import)

```

import InputOtp from 'primevue/inputotp';


```

## Basic [#](https://primevue.org/inputotp/#basic)

InputOtp is used with the *v-model* property for two-way value binding. The number of characters is defined with the *length* option, which is set to 4 by default.

```

<InputOtp v-model="value" />


```

## Forms [#](https://primevue.org/inputotp/#forms)

InputOtp integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <InputOtp name="passcode" />
        <Message v-if="$form.passcode?.invalid" severity="error" size="small" variant="simple">{{ $form.passcode.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Mask [#](https://primevue.org/inputotp/#mask)

Enable the *mask* option to hide the values in the input fields.

```

<InputOtp v-model="value" mask />


```

## Integer Only [#](https://primevue.org/inputotp/#integeronly)

When *integerOnly* is present, only integers can be accepted as input.

```

<InputOtp v-model="value" integerOnly />


```

## Filled [#](https://primevue.org/inputotp/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

```

<InputOtp v-model="value" variant="filled" />


```

## Sizes [#](https://primevue.org/inputotp/#sizes)

InputOtp provides *small* and *large* sizes as alternatives to the base.

```

<InputOtp v-model="value1" size="small" />
<InputOtp v-model="value2" />
<InputOtp v-model="value3" size="large" />


```

## Template [#](https://primevue.org/inputotp/#template)

Define a template with your own UI elements with bindings to the provided events and attributes to replace the default design.

```

<InputOtp v-model="value">
    <template #default="{ attrs, events }">
        <input type="text" v-bind="attrs" v-on="events" class="custom-otp-input" />
    </template>
</InputOtp>


```

## Sample [#](https://primevue.org/inputotp/#sample)

A sample UI implementation with templating and additional elements.

Authenticate Your Account

Please enter the code sent to your phone.

Resend CodeSubmit Code

```

<div class="flex flex-col items-center">
    <div class="font-bold text-xl mb-2">Authenticate Your Account</div>
    <p class="text-surface-500 dark:text-surface-400 block mb-8">Please enter the code sent to your phone.</p>
    <InputOtp v-model="value" :length="6" style="gap: 0">
        <template #default="{ attrs, events, index }">
            <input type="text" v-bind="attrs" v-on="events" class="custom-otp-input" />
            <div v-if="index === 3" class="px-4">
                <i class="pi pi-minus" />
            </div>
        </template>
    </InputOtp>
    <div class="flex justify-between mt-8 self-stretch">
        <Button label="Resend Code" link class="p-0"></Button>
        <Button label="Submit Code"></Button>
    </div>
</div>


```

## Accessibility [#](https://primevue.org/inputotp/#accessibility)

### Screen Reader

Input OTP uses a set of InputText components, refer to the [InputText](https://primevue.org/inputtext) component for more information about the screen reader support.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the input otp. |
| *right arrow* | Moves focus to the next input element. |
| *left arrow* | Moves focus to the previous input element. |
| *backspace* | Deletes the input and moves focus to the previous input element. |