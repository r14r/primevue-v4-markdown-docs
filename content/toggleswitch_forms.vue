<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-48">
    <div class="flex flex-col items-center gap-2">
        <ToggleSwitch name="activation" />
        <Message v-if="$form.activation?.invalid" severity="error" size="small" variant="simple">{{ $form.activation.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>