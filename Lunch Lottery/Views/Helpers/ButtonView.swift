//
//  ButtonView.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 10/17/22.
//

import SwiftUI

struct ButtonView: View {
    var body: some View {
        @Binding var isSet: Bool
        
        ZStack {
            FavoriteButton()
            CancelButton()
        }
    }
}

struct ButtonView_Previews: PreviewProvider {
    static var previews: some View {
        ButtonView(isSet: .constant(true))
    }
}
