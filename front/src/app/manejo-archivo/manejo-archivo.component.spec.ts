import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ManejoArchivoComponent } from './manejo-archivo.component';

describe('ManejoArchivoComponent', () => {
  let component: ManejoArchivoComponent;
  let fixture: ComponentFixture<ManejoArchivoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ManejoArchivoComponent]
    });
    fixture = TestBed.createComponent(ManejoArchivoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
