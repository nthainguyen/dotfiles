#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
	[0] = LAYOUT(KC_Q, KC_W, KC_F, KC_P, KC_G, KC_J, KC_L, KC_U, KC_Y, KC_SCLN, KC_A, KC_R, KC_S, KC_T, KC_D, KC_H, KC_N, KC_E, KC_I, KC_O, KC_Z, KC_X, KC_C, KC_V, KC_B, KC_K, KC_M, KC_COMM, KC_DOT, KC_SLSH, KC_ESC, OSL(2), KC_TAB, KC_LSFT, MO(1), KC_LALT, KC_LCTL, KC_SPC, KC_LGUI, KC_MINS, KC_QUOT, KC_ENT),
	[1] = LAYOUT(KC_ASTR, KC_7, KC_8, KC_9, KC_PGUP, KC_LPRN, KC_RPRN, KC_UP, KC_AT, KC_EXLM, KC_PLUS, KC_4, KC_5, KC_6, KC_PGDN, KC_DLR, KC_LEFT, KC_DOWN, KC_RGHT, KC_BSPC, KC_BSLS, KC_1, KC_2, KC_3, KC_0, KC_AMPR, KC_LCBR, KC_RCBR, KC_LBRC, KC_RBRC, KC_NO, KC_NO, KC_LSFT, KC_TRNS, KC_TRNS, KC_LALT, KC_LCTL, KC_ENT, KC_LGUI, KC_RSFT, KC_NO, KC_EQL),
	[2] = LAYOUT(KC_INS, KC_AMPR, KC_ASTR, KC_NO, KC_UNDS, KC_UP, KC_F7, KC_F8, KC_F9, KC_F10, KC_DEL, KC_DLR, KC_PERC, KC_CIRC, KC_PLUS, KC_DOWN, KC_F4, KC_F5, KC_F6, KC_F11, KC_GRV, KC_EXLM, KC_AT, KC_HASH, KC_GRV, KC_TILD, KC_F1, KC_F2, KC_F3, KC_F12, KC_TRNS, KC_NO, KC_LGUI, KC_LSFT, KC_NO, KC_LCTL, KC_LALT, KC_NO, KC_NO, KC_PSCR, KC_SLCK, KC_PAUS)
};