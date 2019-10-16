#include QMK_KEYBOARD_H

//Tap Dance Declarations
enum {
  TD_LODASH = 0
};

//Tap Dance Definitions
qk_tap_dance_action_t tap_dance_actions[] = {
  //Tap once for Esc, twice for Caps Lock
  [TD_LODASH]  = ACTION_TAP_DANCE_DOUBLE(KC_UNDS, KC_MINS)
// Other declarations would go here, separated by commas, if you have them
};


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
	[0] = LAYOUT(KC_Q, KC_W, KC_F, KC_P, KC_G, KC_J, KC_L, KC_U, KC_Y, KC_SCLN, KC_A, KC_R, KC_S, KC_T, KC_D, KC_H, KC_N, KC_E, KC_I, KC_O, KC_Z, KC_X, KC_C, KC_V, KC_B, KC_K, KC_M, KC_COMM, KC_DOT, KC_SLSH, KC_GESC, LT(3,KC_TAB), KC_LALT, OSM(MOD_LSFT), LT(2,KC_BSPC), MO(1), KC_LGUI, KC_SPC, OSM(MOD_LCTL), TD(TD_LODASH), KC_LEAD, KC_SFTENT),
	[1] = LAYOUT(KC_ESC, KC_WH_U, KC_WBAK, KC_WFWD, KC_ESC, KC_PGUP, KC_HOME, KC_UP, KC_END, KC_DEL, OSM(MOD_LALT), KC_WH_D, OSM(MOD_LSFT), OSM(MOD_LCTL), KC_TAB, KC_PGDN, KC_LEFT, KC_DOWN, KC_RGHT, KC_BSPC, KC_1, KC_2, KC_3, KC_4, KC_5, KC_6, KC_7, KC_8, KC_9, KC_0, KC_TRNS, TG(3), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_ENT, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS),
	[2] = LAYOUT(KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_GRV, KC_DQUO, KC_QUOT, KC_MINS, KC_PLUS, KC_EQL, OSM(MOD_LALT), KC_TRNS, OSM(MOD_LSFT), OSM(MOD_LCTL), KC_TAB, KC_LBRC, KC_RBRC, KC_LCBR, KC_RCBR, KC_BSLS, KC_EXLM, KC_AT, KC_HASH, KC_DLR, KC_PERC, KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN, KC_TRNS, KC_TRNS, KC_INS, KC_LSFT, KC_BSPC, KC_LCTL, KC_LALT, KC_ENT, KC_TRNS, KC_LGUI, KC_AMPR, KC_NO),
	[3] = LAYOUT(KC_VOLU, KC_F7, KC_F8, KC_F9, KC_F10, KC_UP, KC_7, KC_8, KC_9, KC_TRNS, KC_VOLD, KC_F4, KC_F5, KC_F6, KC_F11, KC_DOWN, KC_4, KC_5, KC_6, KC_TRNS, RESET, KC_F1, KC_F2, KC_F3, KC_F12, KC_PAUS, KC_1, KC_2, KC_3, KC_TRNS, KC_TRNS, TG(3), KC_TRNS, KC_LSFT, KC_BSPC, KC_LCTL, KC_LALT, KC_SPC, KC_0, KC_DOT, KC_SLCK, KC_ENT)
};




LEADER_EXTERNS();

void matrix_scan_user(void) {
    LEADER_DICTIONARY() {
        leading = false;
        leader_end();

        // Replace the sequences below with your own sequences.
        SEQ_ONE_KEY(KC_T) {
            // When I press KC_LEAD and then T, this sends CTRL + SHIFT + T
            SEND_STRING(SS_LCTRL(SS_LSFT("t")));
        }
        SEQ_ONE_KEY(KC_P) {
            SEND_STRING(SS_LCTRL(SS_TAP(X_PGUP)));
        }

        SEQ_ONE_KEY(KC_N) {
            SEND_STRING(SS_LCTRL(SS_TAP(X_PGDOWN)));
        }

		
        SEQ_TWO_KEYS(KC_Q, KC_Q) {
            SEND_STRING(SS_LALT(SS_TAP(X_F4)));
        }		
		
        SEQ_TWO_KEYS(KC_Q, KC_T) {
            SEND_STRING(SS_LCTRL(SS_TAP(X_F4)));
        }	


        SEQ_TWO_KEYS(KC_D, KC_D) {
            SEND_STRING(SS_TAP(X_END));
            SEND_STRING(SS_LSFT(SS_TAP(X_HOME)));
            SEND_STRING(SS_LCTRL("x"));
        }
		
        SEQ_TWO_KEYS(KC_D, KC_W) {
            SEND_STRING(SS_LCTRL(SS_LSFT(SS_TAP(X_LEFT))));
            SEND_STRING(SS_LCTRL("x"));
        }
		
		SEQ_TWO_KEYS(KC_D, KC_P) {
			SEND_STRING(SS_LCTRL(SS_TAP(X_DOWN)));
            SEND_STRING(SS_LCTRL(SS_LSFT(SS_TAP(X_UP))));
            SEND_STRING(SS_LCTRL("x"));
        }		
		
		
		
        SEQ_TWO_KEYS(KC_C, KC_D) {
            SEND_STRING(SS_TAP(X_END));
            SEND_STRING(SS_LSFT(SS_TAP(X_HOME)));
            SEND_STRING(SS_LCTRL("c"));
        }
		
        SEQ_TWO_KEYS(KC_C, KC_W) {
            SEND_STRING(SS_LCTRL(SS_LSFT(SS_TAP(X_LEFT))));
            SEND_STRING(SS_LCTRL("c"));
        }
		
		SEQ_TWO_KEYS(KC_C, KC_P) {
			SEND_STRING(SS_LCTRL(SS_TAP(X_DOWN)));
            SEND_STRING(SS_LCTRL(SS_LSFT(SS_TAP(X_UP))));
            SEND_STRING(SS_LCTRL("c"));
        }

    }
}
