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