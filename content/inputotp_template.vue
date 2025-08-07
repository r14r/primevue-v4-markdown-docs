<InputOtp v-model="value">
    <template #default="{ attrs, events }">
        <input type="text" v-bind="attrs" v-on="events" class="custom-otp-input" />
    </template>
</InputOtp>