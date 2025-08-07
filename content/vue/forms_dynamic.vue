<Fieldset legend="Form 1" pt:content:class="flex justify-center">
    <DynamicForm @submit="onFormSubmit('Form 1', $event)">
        <DynamicFormField groupId="userId_1" name="username">
            <DynamicFormLabel>Username</DynamicFormLabel>
            <DynamicFormControl defaultValue="PrimeVue" fluid :schema="userNameSchema" />
            <DynamicFormMessage />
        </DynamicFormField>
        <DynamicFormField groupId="passId_1" name="password">
            <DynamicFormLabel>Password</DynamicFormLabel>
            <DynamicFormControl as="Password" :feedback="false" toggleMask fluid :schema="passwordSchema" />
            <DynamicFormMessage errorType="minimum" />
            <DynamicFormMessage errorType="maximum" />
            <DynamicFormMessage errorType="uppercase" severity="warn" />
            <DynamicFormMessage errorType="lowercase" severity="warn" />
            <DynamicFormMessage errorType="number" severity="secondary" />
        </DynamicFormField>
        <DynamicFormSubmit />
    </DynamicForm>
</Fieldset>

<Fieldset legend="Form 2" pt:content:class="flex justify-center">
    <DynamicForm :fields @submit="onFormSubmit('Form 2', $event)" />
</Fieldset>