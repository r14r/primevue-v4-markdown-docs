<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <InputOtp name="passcode" />
        <Message v-if="$form.passcode?.invalid" severity="error" size="small" variant="simple">{{ $form.passcode.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>